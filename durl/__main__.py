import click

from . import util


@click.command()
@click.option('-r', '--name', help='repo name')
@click.option('-f', 'is_file_search', is_flag=True, help='search for files')
@click.argument('keyword')
def main(name, is_file_search, keyword):
    repo = util.get_repos()[name]
    if is_file_search:
        got = util.find(repo.path, keyword)
    else:
        got = util.grep(repo.path, keyword)
    if not got:
        print('No match!')

    for line in got:
        if is_file_search:
            print(util.format_output(repo.url, line))
        else:
            line, n = line.split(':')[:2]
            print(util.format_output(repo.url, line, linenumber=n))


if __name__ == '__main__':
    main()
