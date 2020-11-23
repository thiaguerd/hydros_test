FROM node

FROM python:3.9.0

COPY --from=0 /usr/local/bin/node /usr/local/bin/
COPY --from=0 /usr/local/lib/node_modules /usr/local/lib/node_modules
COPY --from=0 /opt/ /opt/

RUN ln -sf /usr/local/bin/node /usr/local/bin/nodejs \
  && ln -sf ../lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm \
  && ln -sf ../lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx \
  && ln -sf /opt/yarn*/bin/yarn /usr/local/bin/yarn \
  && ln -sf /opt/yarn*/bin/yarnpkg /usr/local/bin/yarnpkg

COPY scripts/setup.sh /usr/bin/setup

RUN chmod +x /usr/bin/setup

WORKDIR /app

RUN python3 -m venv venv

RUN . ./venv/bin/activate

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
