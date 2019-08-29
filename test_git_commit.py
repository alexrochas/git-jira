from unittest import TestCase
import git_commit


class TestGitCommit(TestCase):

    def test_should_parse_branch_name(self):
        branch_name = "GB-1234 something random"
        ticket_number = git_commit.extract_ticket_number(branch_name)
        self.assertEqual(ticket_number, "GB-1234")

    def test_should_return_first_match(self):
        branch_name = "GB-1234 something GB-4321 random GB-5432"
        ticket_number = git_commit.extract_ticket_number(branch_name)
        self.assertEqual(ticket_number, "GB-1234")

    def test_should_ignore_case(self):
        branch_name = "gb-1234 something random"
        ticket_number = git_commit.extract_ticket_number(branch_name)
        self.assertEqual(ticket_number, "gb-1234")


