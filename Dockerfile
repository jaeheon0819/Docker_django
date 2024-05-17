# Python 이미지 사용
FROM python:3.10

# 필요한 패키지를 설치
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev

# 작업 디렉토리를 설정
WORKDIR /code

# 필요한 패키지를 복사, 설치
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일을 복사
COPY . /code/

# 정적 파일을 수집
RUN python manage.py collectstatic --noinput

# 컨테이너가 실행될 때 실행할 명령을 설정
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
