# Rapport LAB 0 - LOG 430
Author : Kylian Pasquereau PASK76310301

## Question 1 :
- Si l’un des tests échoue à cause d’un bug, comment pytest signale-t-il l’erreur et aide-t-il à la localiser ? Rédigez un test qui provoque volontairement une erreur, puis montrez la sortie du terminal obtenue.

Lorsqu'un test
Lors d'une erreur, Pytest va montrer le ou les tests ayant eu un problème et va indiquer la sortie attendue de ce test et celle reçue. Les 2 sorties vont être comparées et les différences vont être mises en valeur pour être repérées plus facilement par le développeur.

Test provoquant une erreur :
```py
def test_addition():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5
    assert my_calculator.addition(-1, 1) == 6
    assert my_calculator.addition(-1, -1) == -2
```


```bash
__________________________________________________________________________________________________________________test_addition__________________________________________________________________________________________________________________ 

    def test_addition():
        my_calculator = Calculator()
        assert my_calculator.addition(2, 3) == 5
>       assert my_calculator.addition(-1, 1) == 6
E       assert 0 == 6
E        +  where 0 = addition(-1, 1)
E        +    where addition = <calculator.Calculator object at 0x0000020936518910>.addition

tests\test_calculator.py:21: AssertionError
```

## Question 2 : 
-  Que fait GitHub pendant les étapes de « setup » et « checkout » ? Veuillez inclure la sortie du terminal GitHub CI dans votre réponse.

Pendant la phase de Setup, GitHub va lister les spécifications du système telles que le système d'exploitation et sa version, les détails sur les images utilisées. Ces informations vont être utilisées pour installer l'environnement dans lequel notre application va s'exécuter.

Dans la seconde partie Checkout, GitHub va se charger supprimer l'ancienne version du repository présentee puis va pull la nouvelle version ayant déclenchée le workflow.

Contenu de l'exécution du Setup : 
```bash

Current runner version: '2.328.0'
Runner Image Provisioner
  Hosted Compute Agent
  Version: 20250829.383
  Commit: 27cb235aab5b0e52e153a26cd86b4742e89dac5d
  Build Date: 2025-08-29T13:48:48Z
Operating System
  Ubuntu
  24.04.3
  LTS
Runner Image
  Image: ubuntu-24.04
  Version: 20250907.24.1
  Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20250907.24/images/ubuntu/Ubuntu2404-Readme.md
  Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20250907.24
GITHUB_TOKEN Permissions
  Actions: write
  Attestations: write
  Checks: write
  Contents: write
  Deployments: write
  Discussions: write
  Issues: write
  Metadata: read
  Models: read
  Packages: write
  Pages: write
  PullRequests: write
  RepositoryProjects: write
  SecurityEvents: write
  Statuses: write
Secret source: Actions
Prepare workflow directory
Prepare all required actions
Getting action download info
Download action repository 'actions/checkout@v3' (SHA:f43a0e5ff2bd294095638e18286ca9a3d1956744)
Download action repository 'actions/setup-python@v4' (SHA:7f4fc3e22c37d6ff65e88745f38bd3157c663f7c)
Complete job name: build
```

Contenu de l'exécution du Checkout (le contenu de "Fetching the repository" n'a pas été développé en raison du grand nombre de lignes similaires montrant l'avancement du téléchargement du repository):
```bash
Run actions/checkout@v3
  with:
    repository: Kiroky14/log430-a25-labo0
    token: ***
    ssh-strict: true
    persist-credentials: true
    clean: true
    sparse-checkout-cone-mode: true
    fetch-depth: 1
    fetch-tags: false
    lfs: false
    submodules: false
    set-safe-directory: true
Syncing repository: Kiroky14/log430-a25-labo0
Getting Git version info
  Working directory is '/home/runner/work/log430-a25-labo0/log430-a25-labo0'
  /usr/bin/git version
  git version 2.51.0
Temporarily overriding HOME='/home/runner/work/_temp/b8942e0d-01db-4a99-a2c0-97640b250fbb' before making global git config changes
Adding repository directory to the temporary git global config as a safe directory
/usr/bin/git config --global --add safe.directory /home/runner/work/log430-a25-labo0/log430-a25-labo0
Deleting the contents of '/home/runner/work/log430-a25-labo0/log430-a25-labo0'
Initializing the repository
  /usr/bin/git init /home/runner/work/log430-a25-labo0/log430-a25-labo0
  hint: Using 'master' as the name for the initial branch. This default branch name
  hint: is subject to change. To configure the initial branch name to use in all
  hint: of your new repositories, which will suppress this warning, call:
  hint:
  hint: 	git config --global init.defaultBranch <name>
  hint:
  hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
  hint: 'development'. The just-created branch can be renamed via this command:
  hint:
  hint: 	git branch -m <name>
  hint:
  hint: Disable this message with "git config set advice.defaultBranchName false"
  Initialized empty Git repository in /home/runner/work/log430-a25-labo0/log430-a25-labo0/.git/
  /usr/bin/git remote add origin https://github.com/Kiroky14/log430-a25-labo0
Disabling automatic garbage collection
  /usr/bin/git config --local gc.auto 0
Setting up auth
  /usr/bin/git config --local --name-only --get-regexp core\.sshCommand
  /usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
  /usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
  /usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
  /usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
Fetching the repository
Determining the checkout info
Checking out the ref
  /usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
  Switched to a new branch 'main'
  branch 'main' set up to track 'origin/main'.
/usr/bin/git log -1 --format='%H'
'8e438ac065379a923a9704ca2b92d4bf02bae532'
```

## Question 3 : 
- Quel approache et quelles commandes avez-vous exécutées pour automatiser le déploiement continu de l'application dans la machine virtuelle ? Veuillez inclure les sorties du terminal et les scripts bash dans votre réponse.

Cette question n'a pas pu être répondue, la VM n'étant pas accessible au moment où le laboratoire s'est déroulé je me suis retrouvé bloqué à cette étape.

preuve : 
```bash
$ ssh log430-etudiante-68@10.194.32.187
log430-etudiante-68@10.194.32.187's password:
Permission denied, please try again.
log430-etudiante-68@10.194.32.187's password:
```

Je joins aussi un message de Mr Gabriel C. Ullmann indiquant que plusieurs étudiants faisaient face à ce problème et que les questions 3 et 4 on été laissées : 

```text
Le 10 septembre 2025 : 

Gabriel C. Ullmann — 20:04
@Fabio Petrillo Malheureusement, les machines virtuelles n'ont pas fonctionné pour plusieurs personnes.
[20:05]
J'ai recommendé qu'on oublie les questions 3 et 4, ce sont les activités de mise en place du processus de CD. (modifié)
[20:06]
Pour ceux qu'on l'accès au VM, vous pouvez déploier manuellement. Sinon, vous pouvez utiliser une VM Azure, ou n'importe quelle autre. Sinon, malhereusement on a pas des alternatives pour le CD.
```