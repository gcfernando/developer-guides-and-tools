# Keep repository-only files reachable from pages whose permalinks differ from source paths.
require "pathname"
require "cgi"

Jekyll::Hooks.register :pages, :post_render do |page|
  next unless page.output_ext == ".html"
  site = page.site
  source = File.expand_path(site.source)
  page.output = page.output.gsub(/(\bhref=["'])([^"'#][^"']*)(["'])/) do
    prefix, url, closing = Regexp.last_match.captures
    next prefix + url + closing if url.match?(%r{\A(?:[a-z][a-z0-9+.-]*:|/)}i)
    pathname, fragment = url.split("#", 2)
    target = File.expand_path(CGI.unescape(pathname), File.dirname(File.join(source, page.path)))
    next prefix + url + closing unless target.start_with?(source + "/") || target.start_with?(source + File::SEPARATOR)
    relative = Pathname.new(target).relative_path_from(Pathname.new(source)).to_s.tr("\\", "/")
    excluded = site.config.fetch("exclude", []).any? { |item| relative == item || relative.start_with?(item + "/") }
    if File.exist?(target) && (excluded || File.directory?(target))
      kind = File.directory?(target) ? "tree" : "blob"
      prefix + "https://github.com/" + site.config.fetch("repository") + "/" + kind + "/main/" + relative + (fragment ? "#" + fragment : "") + closing
    else
      prefix + url + closing
    end
  end
end
