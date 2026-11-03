"""Optional model integration lesson. Mock mode is fully offline.

RealModel intentionally has no provider API implementation. The learner supplies
one using their provider's current official SDK and account. It may cost money.
Never paste API keys into this file, evidence notes, logs or progress backups.
"""
import json
from math import isfinite
from time import perf_counter

SCHEMA = {
    'type': 'object',
    'properties': {'answer': {'type': 'string'}, 'source': {'type': ['string', 'null']}},
    'required': ['answer', 'source'],
    'additionalProperties': False,
}


class MockModel:
    def generate(self, prompt):
        if prompt == 'malformed':
            return '{answer: missing quotes}'
        return json.dumps({'answer': 'Open 09:00–17:00.', 'source': 'public-hours'}, ensure_ascii=False)


class RealModel:
    def generate(self, prompt):
        raise NotImplementedError('Fill in a provider adapter using its current official documentation; an account and charges may apply.')


def validate_response(text):
    """Validate exactly SCHEMA above, not arbitrary JSON Schema documents."""
    value = json.loads(text)
    if not isinstance(value, dict) or set(value) != {'answer', 'source'}:
        raise ValueError('Expected exactly answer and source fields')
    if not isinstance(value['answer'], str):
        raise ValueError('answer must be a string')
    if value['source'] is not None and not isinstance(value['source'], str):
        raise ValueError('source must be a string or null')
    return value


def estimate_cost(input_tokens, output_tokens, input_rate_per_million, output_rate_per_million):
    """Learner supplies current published rates in one consistent currency.

    This simple estimate excludes cached, reasoning, batch and tool charges,
    taxes and provider-specific billing rules. Actual billing is authoritative.
    """
    if any(type(v) is not int or v < 0 for v in (input_tokens, output_tokens)):
        raise ValueError('Token counts must be nonnegative integers')
    if any(type(v) not in (int, float) or not isfinite(v) or v < 0
           for v in (input_rate_per_million, output_rate_per_million)):
        raise ValueError('Rates must be finite nonnegative numbers')
    return (input_tokens*input_rate_per_million + output_tokens*output_rate_per_million)/1_000_000


def observe(model, prompt='hours'):
    observations = []
    for _ in range(3):
        started = perf_counter()
        text = model.generate(prompt)
        elapsed = perf_counter()-started
        observations.append({'response': validate_response(text), 'seconds': elapsed})
    return observations


if __name__ == '__main__':
    for observation in observe(MockModel()):
        print(observation)
    try:
        validate_response(MockModel().generate('malformed'))
    except (ValueError, TypeError) as error:
        print('Rejected malformed response:', type(error).__name__)
    print('Mock outputs match by design. Latencies are local measurements, not provider latency estimates.')
