from pydantic import BaseModel,Field
from typing import Annotated,Literal

class UserInput(BaseModel):
    Age: Annotated[int, Field(..., description="Age of the employee",ge=18,le=80)]

    BusinessTravel: Annotated[
        Literal["Travel_Rarely", "Travel_Frequently", "Non-Travel"],
        Field(..., description="Business travel frequency")
    ]

    DailyRate: Annotated[
        int,
        Field(default=800, description="Daily rate of the employee")
    ]

    Department: Annotated[
        Literal["Sales", "Research & Development", "Human Resources"],
        Field(..., description="Department of the employee")
    ]

    DistanceFromHome: Annotated[
        int,
        Field(..., description="Distance from home in kilometers",ge=0)
    ]

    Education: Annotated[
        int,
        Field(default=3, description="Education level (1-5)",ge=1,le=5)
    ]

    EducationField: Annotated[
        Literal[
            "Life Sciences",
            "Other",
            "Medical",
            "Marketing",
            "Technical Degree",
            "Human Resources"
        ],
        Field(default="Life Sciences", description="Educational background")
    ]

    EnvironmentSatisfaction: Annotated[
        int,
        Field(..., description="Environment satisfaction level (1-4)",ge=1,le=4)
    ]

    Gender: Annotated[
        Literal["Male", "Female"],
        Field(default="Male", description="Gender of the employee")
    ]

    HourlyRate: Annotated[
        int,
        Field(default=66, description="Hourly rate of the employee",ge=0)
    ]

    JobInvolvement: Annotated[
        int,
        Field(default=3, description="Job involvement level (1-4)",ge=1,le=4)
    ]

    JobLevel: Annotated[
        int,
        Field(default=2, description="Job level",ge=1,le=5)
    ]

    JobRole: Annotated[
        Literal[
            "Sales Executive",
            "Research Scientist",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Manager",
            "Sales Representative",
            "Research Director",
            "Human Resources"
        ],
        Field(default="Sales Executive", description="Job role of the employee")
    ]

    JobSatisfaction: Annotated[
        int,
        Field(..., description="Job satisfaction level (1-4)",ge=1,le=4)
    ]

    MaritalStatus: Annotated[
        Literal["Single", "Married", "Divorced"],
        Field(..., description="Marital status")
    ]

    MonthlyIncome: Annotated[
        int,
        Field(..., description="Monthly income of the employee",ge=0)
    ]

    MonthlyRate: Annotated[
        int,
        Field(default=14000, description="Monthly rate",ge=0)
    ]

    NumCompaniesWorked: Annotated[
        int,
        Field(default=2, description="Number of companies worked",ge=0,le=15)
    ]

    OverTime: Annotated[
        Literal["Yes", "No"],
        Field(..., description="Whether the employee works overtime")
    ]

    PercentSalaryHike: Annotated[
        int,
        Field(default=14, description="Percentage salary hike",ge=0,le=100)
    ]

    PerformanceRating: Annotated[
        Literal[3,4],
        Field(default=3, description="Performance rating (3 or 4)")
    ]

    RelationshipSatisfaction: Annotated[
        int,
        Field(default=3, description="Relationship satisfaction level (1-4)",ge=1,le=4)
    ]

    StockOptionLevel: Annotated[
        int,
        Field(default=1, description="Stock option level (0-3)",ge=0,le=3)
    ]

    TotalWorkingYears: Annotated[
        int,
        Field(default=8, description="Total years of work experience",ge=0)
    ]

    TrainingTimesLastYear: Annotated[
        int,
        Field(default=3, description="Training sessions attended last year")
    ]

    WorkLifeBalance: Annotated[
        int,
        Field(..., description="Work-life balance level (1-4)",ge=1,le=4)
    ]

    YearsAtCompany: Annotated[
        int,
        Field(..., description="Years worked at the current company",ge=0)
    ]

    YearsInCurrentRole: Annotated[
        int,
        Field(default=4, description="Years in the current role",ge=0)
    ]

    YearsSinceLastPromotion: Annotated[
        int,
        Field(..., description="Years since last promotion",ge=0)
    ]

    YearsWithCurrManager: Annotated[
        int,
        Field(default=4, description="Years with the current manager",ge=0)
    ]
    
    

