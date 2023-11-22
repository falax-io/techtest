FROM mcr.microsoft.com/playwright/python:v1.39.0-jammy AS runner

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install git+https://github.com/behave/behave
#RUN pip install pytest-playwright
RUN pip install behave-html-formatter
#RUN playwright install
RUN behave -f html -o behave-report.html || echo "Tests failed"

FROM nginx:alpine

COPY --from=0 /app/behave-report.html /usr/share/nginx/html/report/index.html

