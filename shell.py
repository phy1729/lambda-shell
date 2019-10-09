#!/usr/bin/env python3
"""Local shell interface for lambda-shell."""
import json
import shlex
import sys

import requests


def get_endpoint():
    """Return lambda-shell endpoint from terrafrom state."""
    try:
        with open('terraform.tfstate', 'r') as stream:
            state = json.load(stream)
    except FileNotFoundError:
        return None

    try:
        endpoint = state['outputs']['shell_endpoint']['value']
    except KeyError:
        return None

    return endpoint


def main():
    """Run local shell interface for lambda-shell."""
    endpoint = get_endpoint()

    while True:
        try:
            line = input('> ')
        except EOFError:
            print('')
            break
        try:
            args = shlex.split(line)
        except ValueError as err:
            print(f'Error: {err}', file=sys.stderr)
            continue

        if not args:
            continue

        if args[0] == 'exit':
            break

        if len(args) < 2:
            print('usage: service action [--flag value ...]',
                  file=sys.stderr)
            continue

        request = {'client_args': {'service_name': args[0]},
                   'action': args[1],
                   'args': {}}

        args = args[2:]
        iter_args = iter(args)
        for flag in iter_args:
            value = next(iter_args)
            if not flag.startswith('--'):
                print(f'Invalid flag: {flag}', file=sys.stderr)
                continue

            request['args'][flag[2:]] = value

        resp = requests.post(endpoint,
                             data=json.dumps(request)).json()
        json.dump(resp, sys.stdout, indent=4)
        print('')


if __name__ == '__main__':
    main()
