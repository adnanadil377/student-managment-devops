from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Student Management API")

app.add_middleware(
	CORSMiddleware,
	allow_origins=[
		"http://localhost:5173",
		"http://127.0.0.1:5173",
		"http://localhost",
		"http://localhost:80",
		"http://frontend",
	],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/api/student")
def get_student() -> dict[str, str]:
	return {
		"student_name": "Adnan Omar",
		"roll_number": "2023BCS0035",
	}
