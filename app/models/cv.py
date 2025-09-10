from pydantic import BaseModel
from typing import List, Optional


class Job(BaseModel):
    position: str
    company: str
    years: str


class Education(BaseModel):
    degree: str
    school: str
    year: str


class ContactInfo(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    website_link: Optional[str] = None

    @property
    def website_base(
        self,
    ) -> Optional[str]:  # Extract base URL to avoid show UTM parameters
        if self.website_link:
            from urllib.parse import urlparse

            parsed = urlparse(self.website_link)
            return (
                f"{parsed.scheme}://{parsed.netloc}"
                if parsed.scheme and parsed.netloc
                else parsed.netloc or self.website_link
            )
        return None


class CV(BaseModel):
    name: str
    titles: List[str]
    work_experience: List[Job]
    skills: List[str]
    education: List[Education]
    contact_info: ContactInfo
