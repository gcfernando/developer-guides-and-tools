"""Regression checks for complete agent-team guide examples and downloads."""

from html import unescape
from pathlib import Path
import re
import tomllib
import unittest
import zipfile


BASE = Path(__file__).resolve().parents[1] / 'apps' / 'ai-agent-team-guides'
PRODUCTS = {
    'claude': ('claude-code', '.claude'),
    'codex': ('openai-codex', '.agents'),
    'copilot': ('github-copilot', '.github'),
}


class CompleteTeamGuides(unittest.TestCase):
    def test_codex_model_and_global_controls_are_explicit(self):
        root = BASE / 'templates' / 'codex'
        config = tomllib.loads((root / '.codex/config.toml').read_text())
        self.assertEqual(config['model'], 'gpt-6.1-sol')
        self.assertEqual(config['model_reasoning_effort'], 'medium')
        self.assertEqual(config['sandbox_mode'], 'workspace-write')
        self.assertEqual(config['approval_policy'], 'on-request')
        self.assertIs(config['agents']['enabled'], True)
        self.assertEqual(config['agents']['max_concurrent_threads_per_session'], 3)
        self.assertEqual(config['agents']['default_subagent_model'], 'gpt-6.1-sol')
        for role in ['developer', 'qa-tester', 'devops']:
            agent = tomllib.loads((root / '.codex/agents' / f'{role}.toml').read_text())
            self.assertEqual(agent['name'], role)
            self.assertEqual(agent['model'], 'gpt-6.1-sol')
            self.assertEqual(agent['model_reasoning_effort'], 'medium')
            self.assertIn('.agent-team/recovery.md', agent['developer_instructions'])

    def test_each_displayed_file_and_download_matches_its_source(self):
        for product, (page, _) in PRODUCTS.items():
            with self.subTest(product=product):
                root = BASE / 'templates' / product
                source = (BASE / f'{page}-guide.html').read_text(encoding='utf-8')
                blocks = re.findall(r'<figure class="code k-file">.*?<span class="lab">(.*?)</span>.*?<code>(.*?)</code>', source, re.S)
                displayed = {unescape(label): unescape(body).strip() for label, body in blocks}
                expected = {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob('*') if p.is_file()}
                for name, data in expected.items():
                    if name != 'README.md':
                        self.assertIn(name, displayed)
                        self.assertEqual(displayed[name], data.decode('utf-8').strip(), name)
                with zipfile.ZipFile(BASE / 'downloads' / f'{product}-team.zip') as archive:
                    self.assertEqual(expected, {n: archive.read(n) for n in archive.namelist()})
                    self.assertIsNone(archive.testzip())
                for extension in ['ps1', 'sh']:
                    script = (BASE / 'scripts' / f'{product}-setup-practice.{extension}').read_text(encoding='utf-8')
                    pattern = (r"^W '([^']+)' @'\n(.*?)\n'@" if extension == 'ps1' else
                               r"^w '([^']+)' <<'END_OF_FILE'\n(.*?)\nEND_OF_FILE")
                    embedded = dict(re.findall(pattern, script, re.S | re.M))
                    for name, data in expected.items():
                        if name != 'README.md':
                            self.assertEqual(embedded[name].strip(), data.decode('utf-8').strip(), (extension, name))

    def test_yaml_agent_examples_include_the_selected_settings(self):
        for product in ['claude', 'copilot']:
            folder = '.claude' if product == 'claude' else '.github'
            for path in (BASE / 'templates' / product / folder / 'agents').glob('*.md'):
                with self.subTest(path=path):
                    header = path.read_text(encoding='utf-8').split('---', 2)[1]
                    model = ('opus' if path.stem == 'lead' else 'sonnet') if product == 'claude' else 'gpt-6.1-sol'
                    self.assertRegex(header, rf'(?m)^model: {re.escape(model)}$')
                    self.assertRegex(header, r'(?m)^tools: .+')
                    if product == 'claude':
                        self.assertRegex(header, r'(?m)^effort: medium$')
                        self.assertRegex(header, r'(?m)^permissionMode: default$')
                    else:
                        self.assertRegex(header, r'(?m)^reasoningEffort: medium$')
                        self.assertRegex(header, r'(?m)^modelPolicy: preferred$')
                        self.assertRegex(header, r'(?m)^include-custom-instructions: true$')

    def test_skill_metadata_is_product_specific(self):
        for product, (_, folder) in PRODUCTS.items():
            skill = BASE / 'templates' / product / folder / 'skills/team-plan/SKILL.md'
            text = skill.read_text(encoding='utf-8')
            header = text.split('---', 2)[1]
            if product == 'codex':
                self.assertNotRegex(header, r'(?m)^(model|allowed-tools|user-invocable):')
                companion = skill.parent / 'agents/openai.yaml'
                self.assertIn('allow_implicit_invocation: true', companion.read_text())
            else:
                self.assertRegex(header, r'(?m)^user-invocable: true$')
                self.assertRegex(header, r'(?m)^disable-model-invocation: false$')
                self.assertRegex(header, r'(?m)^allowed-tools: .+')
                if product == 'claude':
                    self.assertRegex(header, r'(?m)^model: opus$')
                    self.assertRegex(header, r'(?m)^effort: medium$')
                else:
                    self.assertNotRegex(header, r'(?m)^(model|reasoningEffort):')

    def test_examples_have_one_source_for_recovery_limits(self):
        for product in PRODUCTS:
            root = BASE / 'templates' / product
            for name in ['.agent-team/project.md', '.agent-team/roles/developer.md']:
                text = (root / name).read_text(encoding='utf-8')
                self.assertIn('.agent-team/recovery.md', text)
                self.assertNotIn('at most two', text)
                self.assertNotIn('at most one', text)
            recovery = (root / '.agent-team/recovery.md').read_text(encoding='utf-8')
            self.assertIn('Same-action retry: at most 1', recovery)
            self.assertIn('whole user request: at most 2', recovery)

    def test_folder_trees_and_download_controls_are_complete(self):
        for product, (page, _) in PRODUCTS.items():
            source = (BASE / f'{page}-guide.html').read_text(encoding='utf-8')
            self.assertNotIn('Rewritten 9 November 2026', source)
            self.assertIn(f'<a download href="downloads/{product}-team.zip">', source)
            tree = unescape(re.search(r'Folder tree.*?<code>(.*?)</code>', source, re.S)[1])
            if product == 'codex':
                self.assertIn('config.toml', tree)
                self.assertIn('team-plan/agents/openai.yaml', tree)
            if product == 'claude':
                self.assertIn('CLAUDE.md', tree)
                self.assertIn('settings.json', tree)
            if product != 'copilot':
                self.assertNotIn('Copilot CLI needs PowerShell', source)


if __name__ == '__main__':
    unittest.main()
