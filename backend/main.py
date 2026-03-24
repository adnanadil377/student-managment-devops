from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Student Management API")

origins_env = os.getenv(
	"ALLOWED_ORIGINS",
	"http://localhost:5173,http://127.0.0.1:5173,http://localhost,http://127.0.0.1",
)
allowed_origins = [origin.strip() for origin in origins_env.split(",") if origin.strip()]

app.add_middleware(
	CORSMiddleware,
	allow_origins=allowed_origins,
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
