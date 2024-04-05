#70 Git y Github   
"""
 * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
 * - Hash
 * - Autor
 * - Mensaje
 * - Fecha y hora
 *
 * Ejemplo de salida:
 * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.
"""

import os
import git
from datetime import datetime

abspath = os.path.abspath(__file__) #get the file directory
dname = os.path.dirname(abspath)
os.chdir(dname) #change to file directory

repo = git.Repo(os.getcwd())
print(repo)
print(repo.git.rev_parse("HEAD"))

repo.git.show()

ten_first_commits = list(repo.iter_commits(max_count=10))
print(ten_first_commits)

for i in range(10):
    commit = ten_first_commits[i]

    commit_hash = repo.git.show("-s", "--format=Hash: %H", commit.hexsha)
    author = repo.git.show("-s", "--format=Author: %an <%ae>", commit.hexsha)
    message = repo.git.show("-s", "--format=Message: %s", commit.hexsha)
    date = repo.git.show("-s", "--format=%ci", commit.hexsha)

    datetime_object = datetime.strptime(date[0:-6], '%Y-%m-%d %H:%M:%S')
    dateF = datetime_object.strftime('%d-%m-%Y %H:%M:%S')

    print("Commit "+ str(i+1),commit_hash, author, "Date: " + dateF, message)

commit_counter = 1

for commit in list(git.Repo(".").iter_commits())[:10]:
    print(f"Commit {commit_counter} | {commit.hexsha} | {commit.author.name} | {commit.message} | {commit.authored_datetime}".replace("\n", ""))
    commit_counter += 1