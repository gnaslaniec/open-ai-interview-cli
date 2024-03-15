import subprocess
from click.testing import CliRunner
from interview_ai import cli

def test_cli_succeeds_with_help_flag():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ['--help'])
    assert result.exit_code == 0


def test_cli_succeeds_with_valid_args():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ['tests/test_pdfs/dummy.pdf', '--role', 'Software Engineer', '--num-questions', '3'])
    assert result.exit_code == 0


def test_cli_fails_with_invalid_file():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ['invalid_file.xyz', '--role', 'Software Engineer', '--num-questions', '3'])
    assert result.exit_code == 2


def test_cli_fails_with_missing_role():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ['tests/test_pdfs/sample_resume.pdf'])
    assert result.exit_code == 2
