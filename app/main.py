from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import students, courses, lecturers, enrollments, assignments, grades

app = FastAPI(
    title="University Course Management API",
    description="REST API for managing students, courses, lecturers, enrollments, assignments and grades",
    version="0.1.0",
)

# Allow frontend (running on a different port) to talk to the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routers
app.include_router(students.router)
app.include_router(courses.router)
app.include_router(lecturers.router)
app.include_router(enrollments.router)
app.include_router(assignments.router)
app.include_router(grades.router)


@app.get("/")
def root():
    return {
        "message": "University Course Management API",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}