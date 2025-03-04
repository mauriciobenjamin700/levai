from pydantic import BaseModel


class BaseSchema(BaseModel):
    
    def to_dict(self, exclude: list[str]=[]):
        """
        Convert the schema to a dictionary and exclude the keys in the exclude list.
        
        - Args:
            - exclude: list[str]: List of keys to exclude from the dictionary.
        - Returns:
            - dict: Dictionary containing the data of the schema
        """
        
        dict_data = self.model_dump(exclude_none=True)
        
        return {k: v for k, v in dict_data.items() if k not in exclude}
        
        