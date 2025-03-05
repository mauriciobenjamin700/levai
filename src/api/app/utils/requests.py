from httpx import AsyncClient


class Requests:
    """
    Requests class to make async HTTP requests
    
    - Attributes:
        - base_url: str: Base URL of the API
    - Methods:
        - get: dict: Make a GET request
        - post: dict: Make a POST request
        - put: dict: Make a PUT request
        - delete: dict: Make a DELETE request
    """
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def get(self, endpoint: str) -> dict:
        """
        Make a GET request
        
        - Args:
            - endpoint: str: Endpoint to make the request to
        - Returns:
            - dict: JSON response
        """
        async with AsyncClient() as client:
            response = await client.get(f"{self.base_url}/{endpoint}")
            return response.json()
        
        
    async def post(self, endpoint: str, data: dict) -> dict:
        """
        Make a POST request
        
        - Args:
            - endpoint: str: Endpoint to make the request to
            - data: dict: Data to send in the request
        - Returns:
            - dict: JSON response
        """
        async with AsyncClient() as client:
            print(f"{self.base_url}/{endpoint}")
            response = await client.post(f"{self.base_url}/{endpoint}", json=data)
            return response.json()
    
    async def put(self, endpoint: str, data: dict) -> dict:
        """
        Make a PUT request
        
        - Args:
            - endpoint: str: Endpoint to make the request to
            - data: dict: Data to send in the request
        - Returns:
            - dict: JSON response
        """
        async with AsyncClient() as client:
            response = await client.put(f"{self.base_url}/{endpoint}", json=data)
            return response.json()
        
    async def delete(self, endpoint: str) -> dict:
        """
        Make a DELETE request
        
        - Args:
            - endpoint: str: Endpoint to make the request to
        - Returns:
            - dict: JSON response
        """
        async with AsyncClient() as client:
            response = await client.delete(f"{self.base_url}/{endpoint}")
            return response.json()
        
    
    async def post_stream(self, endpoint: str, data: dict):
        """
        Make a POST request with streaming
        
        - Args:
            - endpoint: str: Endpoint to make the request to
            - data: dict: Data to send in the request
        - Returns:
            - dict: JSON response
        """
        async with AsyncClient() as client:
            async with client.stream("POST", f"{self.base_url}/{endpoint}", json=data) as response:
                async for chunk in response.aiter_text():
                    yield chunk
    