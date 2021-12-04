from django.test import TestCase
from vote.models import VoterArea, Candidate, Vote
from django.contrib.auth.models import User


class VoteTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser', 'testuser@testuser.com', 'testuserpassword')
        # self.area = VoterArea.objects.create(name="Area 57", total_voter="1")
        # self.candidate = Candidate.objects.create(name="riva", area=self.area)
        # self.vote = Vote()
        # self.vote.name = "union vote"
        # self.vote.save()
        # self.vote.candidates.add(self.candidate)
        # self.vote.save()

    def test_user_create(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.id, 4)
        self.assertEqual(self.user.email, 'testuser@testuser.com')

    def test_area_create(self):
        pass
        # self.area = VoterArea.objects.create(name="Area 57", total_voter="1")

    def test_update(self):
        pass

    def test_delete(self):
        pass
