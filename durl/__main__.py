import click

from . import util

# repos.csv
# repo1,/a/b/ct/,github
# repo2,/a/b/ct/,opengrok


prefix = 'https://github.com/nosarthur/'

repos = {
        'durl': '/Users/dzhou/src/durl',
        }

@click.command()
@click.option('-r', '--repo', help='repo name')
@click.option('-f', 'is_file_search', is_flag=True, help='search for files')
@click.argument('keyword')
def main(repo, is_file_search, keyword):
    print(repo, is_file_search, keyword)

    path = repos[repo]
    if is_file_search:
        got = util.find(path, keyword)
    else:
        got = util.grep(path, keyword)
    for line in got:
        print(prefix + line)


if __name__ == '__main__':
    main()
