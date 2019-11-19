getopt -o hvad --long help,version, actor, director -n 'moviedb' -- "$@"
VERSION="Simple menu of movie db version: 0.0.1"
HELP_MESSAGE="Usage: movieddb.sh [OPTIONS]

This programm allows you to...

Otions:
-h, --help      Montre l'aide
-v, --version   Montre la version du programme
-a, --actor     Créer une liste actor au format CSV
-d, --director  Créer une liste director au format CSV
"
#On s'assure que les bon paramètres sont entrés.
if [ $2 !=  "a" ] || [ $2 !=  "v" ] || [ $2 !=  "h" ] || [ $2 !=  "d" ]; then
    echo "Merci de regarder les options, interruption du programme"
    exit 1
fi


#Verification de la présence d'actors.json et directors.json
if [ -f actors.json && -f directors.json]; then
    python3 moviedb.py -c #A rajouter nom de base de donnée
else
    echo "Initialisation des bases de données interrompues, interruption du programme"
    exit 3
fi

#Vérification de la présence des répertoire actor et director
if [ ! -f cache/actor && cache/director]; then
    mkdir cache/actor
    mkdir cache/director
fi


#Vérification du fichier CSV ne se trouve pas déja RAJOUTER OPTION -a/--actor
if [ -f "cache/actor/$ACTOR" ]; then
    Rscript stats_name_years.R $ACTOR
else
    python3 moviedb.py $ACTOR > cache/actor
    #Si fichier contient None, RAJOUTER CSV
    if [ cache/actor != 'None']; then
        echo "La personne recherchée n'est pas dans la base"
    else
        #RAJOUTER NOM PDF
        echo "Voici le nom du PDF créé : $PDF"
    fi
fi

# A priori ca, ca marcherait
a=1; d=1; interactive=0;
eval set -- "$GET_OPT"
while true
    do
        case "${1}" in
            -h|--help)
                echo "$HELP_MESSAGE"; exit 0;;
            -v|--version)
                echo "$VERSION"; exit 0;;
            -a|--actor)
                echo "teeeest"; exit 0;;
            -d|--director)
                echo "test"; exit 0;;
            --) shift; break;;
            *) echo "Options ${1} is not a known option."; echo "$HELP_MESSAGE" exit 1;;
        esac
    done