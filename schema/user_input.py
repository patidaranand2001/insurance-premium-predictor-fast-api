
from pydantic import BaseModel, Field, computed_field , field_validator
from typing import Literal, Annotated

# pydantic model to validate incoming data
class UserInput(BaseModel):

    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    gender: Annotated[str, Field(...,  description='sex of the user')]
    bmi: Annotated[float, Field(..., gt=0, description='bmi of user')]
    children: Annotated[int, Field(...,description='Number of children of the user')]
    is_smoker: Annotated[str, Field(..., description='Is user a smoker')]
    p_region: Annotated[str, Field(..., description='The region that the user belongs to')]

    @field_validator('gender','is_smoker','p_region')
    @classmethod
    def validate_category(cls, v:str):
        return v.strip().lower()
    


    @computed_field
    @property
    def sex(self) -> int:
        return 1 if self.gender == 'male' else 0
    
    @computed_field
    @property
    def smoker(self) -> int:
        return 1 if self.is_smoker == 'yes' else 0

    @computed_field
    @property
    def region_northwest(self) -> int:
        return 1 if self.p_region == 'northwest' else 0
    
    @computed_field
    @property
    def region_southeast(self) -> int:
        return 1 if self.p_region == 'southeast' else 0
    
    @computed_field
    @property
    def region_southwest(self) -> int:
        return 1 if self.p_region == 'southwest' else 0
    
    