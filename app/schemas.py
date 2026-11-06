from typing import Annotated

from pydantic import (BaseModel,ConfigDict,StringConstraints)
studentidstr=Annotated[str,StringConstraints(pattern=r"^s\ST{4}$")]
descriptionstr=Annotated[str,StringConstraints(min_length=5,max_length=100)]

class ToolsCreate(BaseModel):
    equipment_id:int
    student_id:studentidstr
    description:descriptionstr
    priority:int

class ToolsRead(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    equipment_id:int
    student_id:studentidstr
    description:descriptionstr
    priority:int