import unittest

from api.client.model import Client
from api.client.repositories import ClientRepositoryABC
from api.client.resolvers import resolve_client


class MockClientRepository(ClientRepositoryABC):
    async def get_client(self, id: str) -> Client:
        return Client(
            id="CL_TESTID",
            name="TEST CLIENT",
        )

class TestResolvers(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.repository = MockClientRepository()

    async def test_gets_client(self):
        self.assertEqual(
            await resolve_client(
                repository=self.repository,
                id="CL_TESTID",
            ),
            Client(
                id="CL_TESTID",
                name="TEST CLIENT",
            )
        )
