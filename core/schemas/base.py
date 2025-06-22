from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """
    Base schema for all Pydantic models in the application.
    This class can be extended by other schemas to inherit common functionality.
    """
    
    model_config = ConfigDict(
        use_enum_values= True,
        from_attributes= True
    )

    def to_dict(self, exclude: list[str] = [], include: dict = {}) -> dict:
        """
        Convert the Pydantic model instance to a dictionary.

        Args:
            exclude (list[str]): List of fields to exclude from the dictionary.
            include (dict): Dictionary of fields to include in the dictionary.

        Returns:
            dict: Dictionary representation of the Pydantic model instance.
        """
        
        data = {
            key: value for key, value in self.model_dump(exclude_none=True).items()
            if key not in exclude
        }

        if include:
            data.update(include)

        return data
    
    def from_object(self, obj: object) -> "BaseSchema":
        """
        Populate the Pydantic model instance from an object.

        Args:
            obj (object): The object to populate the Pydantic model instance from.

        Returns:
            BaseSchema: The Pydantic model instance populated with data from the object.
        """
        
        return self.model_validate(obj)