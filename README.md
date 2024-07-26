<h1>Fullstack Service Networking Season.2 <br />HyperCorn & FastApi RESTful API Program</h1>	

Server : Python (HyperCorn ASGI Server + FastApi Application)

Client : Web Browser (PyScript : Python in HTML, Pico.css)

Networking : HTTP/1.1, HTTP/2, HTTP/3 (HTTP/3는 '24.7.26 기준 HyperCorn 이슈로 오류 발생)

Packaging : Poetry (추가 패키지: hypercorn, aioquic, h3, fastapi)

<br />
<br />

<h2>실행 방법</h2>	

프로젝트를 다운로드 함

폴더안에서 poetry shell를 실행함<br />
> poetry shell

폴더안에서 필요한 패키지를 설치함<br />
> poetry install

src/server.py를 실행함<br />

> HTTP/1.1
>> poetry run hypercorn server_app:app
> HTTP/2

>> poetry run hypercorn --certfile cert/localhost.crt --keyfile cert/localhost.key --bind localhost:8000 server_app:app

> HTTP/2 & HTTP/3
>> poetry run hypercorn --quic-bind localhost:4433 --certfile cert/localhost.crt --keyfile cert/localhost.key --bind localhost:8000 server_app:app

Chrome browser로 서버에 접속함<br />

> HTTP/1.1
>> http://127.0.0.1:8000/membership_api/

> HTTP/2
>> https://127.0.0.1:8000/membership_api/ 

> HTTP/3
>> https://127.0.0.1:4433/membership_api/ 

화면 위쪽의 “Please wait, program is starting …” 문구가 다음처럼 바뀌기를 기다림<br />
Please fills key/value and executes menu :

CREATE 동작을 위하여,<br />
CREATE 버튼 왼쪽의 Key와 Value에 각각 apple과 1000을 입력하고, CREATE 버튼을 클릭함<br />
CREATE 결과를 웹브라우저 화면과 서버 출력 화면에서 확인함

READ 동작을 위하여,<br />
READ 버튼 왼쪽의 Key에 apple을 입력하고, READ 버튼을 클릭함<br />
READ 결과를 웹브라우저 화면과 서버 출력 화면에서 확인함

UPDATE 동작을 위하여,<br />
UPDATE 버튼 왼쪽의 Key와 Value에 각각 apple과 2000을 입력하고, UPDATE 버튼을 클릭함<br />
UPDATE 결과를 웹브라우저 화면과 서버 출력 화면에서 확인함

DELETE 동작을 위하여,<br />
DELETE 버튼 왼쪽의 Key에 apple을 입력하고, DELETE 버튼을 클릭함<br />
DELETE 결과를 웹브라우저 화면과 서버 출력 화면에서 확인함

서버 종료를 위하여 ctrl-c 키보드 입력을 수행함

Client를 실행하기 위해서, 실행한 Python http.server를 ctrl-c 키보드 입력으로 종료함

Poetry 실행을 중지함<br />
> exit

<br />
<br />

<h2>실행 화면</h2>	

<img src="/screen/client-http1-create.png" width="1000"/>
<img src="/screen/client-http1-read.png" width="1000"/>
<img src="/screen/client-http1-update.png" width="1000"/>
<img src="/screen/client-http1-delete.png" width="1000"/>
<img src="/screen/server-http1.png" width="1000"/>

<img src="/screen/client-http2-create.png" width="1000"/>
<img src="/screen/client-http2-read.png" width="1000"/>
<img src="/screen/client-http2-update.png" width="1000"/>
<img src="/screen/client-http2-delete.png" width="1000"/>
<img src="/screen/server-http2.png" width="1000"/>

<img src="/screen/server-http2-3.png" width="1000"/>
