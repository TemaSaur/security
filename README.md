# GPG

* Установить GPG

sudo apt update; sudo apt install gpg

* Сгенерировать ключи

```bash
$ gpg --full-generate-key
Please select what kind of key you want (RSA)

RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (3072)

GnuPG needs to construct a user ID to identify your key
...
```

```bash
$ gpg --list-secret-keys --keyid-format=long
gpg: checking the trustdb
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
/home/temasaur/.gnupg/pubring.kbx
---------------------------------
sec   rsa3072/63EA7844A843DA94 2024-12-01 [SC]
      AEF9050C5407A8E424AFC48363EA7844A843DA94
uid                 [ultimate] Artemy Vakhrushev (no comment) <temasaur@gmail.com>
ssb   rsa3072/802630B9DBD382FE 2024-12-01 [E]
```

* Зашифровать сообщение/файлы

```bash
$ gpg -e -r "receiver" filename.txt
$ cat filename.txt.gpg
5Io]
    Mic tB1S|_% Ʈ       Fi;l[}d
M{N蚹Őb{)})vǃM,#d4(nq6n ֱtlAjoi"~S'as,?2.p3-a
|8gp)vf3=gzxl
             nRܧ0A31ʇG3a$ee̟v:=JU
                                "\ND]j.@!f
zjfwZ}NeZj3ڞᾇ)̆>!9xxL
Uj[5Pk/.a~:atT  i i&o           ><<
HФ~ek"l8(7dw@VH87T^:0PE
```

```bash
$ echo "message" | gpg -e -r "receiver" -o message.gpg
```

* Дешифровать сообщение/файлы

```bash
$ gpg -d message.gpg
gpg: encrypted with rsa3072 key, ID 35B8F8CA49896F5D, created 2024-12-01
      "receiver <receiver@mail.ru>"
message
```

* Создать и проверить цифровую подпись

```bash
$ gpg --sign filename.txt
$ gpg --verify filename.txt
```

* Проверить файлы на целостность

```bash
$ gpg --sign filename.txt
$ gpg --detach-sign filename.txt
$ gpg --verify filename.txt.sig filename.txt
```

* Экспортировать и импортировать ключи

```bash
$ gpg --export -a "receiver" > receiver_public_key.asc
$ gpg --import receiver_public_key.asc
```

* Реализовать обмен зашифрованными сообщениями

Для обмена зашифрованными сообщениями собеседнику нужно экспортировать свой (открытый) ключ и импортировать этот ключ себе.
После этого сообщения нужно шифровать и дешифровать по имени собеседника (и проверять на целостность).

* Создание меток для ключей

```bash
$ gpg --edit-key "receiver"
gpg> adduid
...
```

* Шифрование файловых архивов и других форматов данных

```bash
gpg -e -r "receiver" archive.tar.gz
```
