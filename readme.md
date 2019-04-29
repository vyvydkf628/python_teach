# 파이썬 기초

>"Life is too short, you need python"

![python](http://story.wisedog.net/wp-content/uploads/2015/02/python_language_logo_300x300.png)

## 0. 파이썬 설치

### 01

1.  [pyenv란?](<https://gist.github.com/edujustin/9792e2206976021079a1df7d7649a3be>)
   - 여러 버젼의 python을 쉽게 __바꿔서 __사용할 수 있게 해주는 도구
2. pyenv 설치과정

```shell
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc

$ exec $SHELL

$pyenv install 3.6.8
$pyenv global 3.6.8
```

## 1. 저장

### 1.1 변수

1. 파이썬에서 = 을 기준으로 오른쪽에 있는 값을 왼쪽에 저장한다

   

   

### 1.2 자료형의 특징

| 문자 | 숫자 | NONE | 참/거짓 |
| ---- | ---- | ---- | ------- |
|      |      |      |         |







