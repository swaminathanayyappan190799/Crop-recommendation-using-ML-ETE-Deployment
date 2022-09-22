FROM python:3
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python", "CropRecommendationApplication.py", "--host=0.0.0.0", "--port=5000"]