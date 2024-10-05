import json
import os

# Obtener datos del secret STUDENT_EMAIL_MAP
STUDENT_EMAIL_MAP = json.loads(os.environ['STUDENT_EMAIL_MAP'])

# Leer el archivo pr_stats.json
with open('pr_stats.json', 'r') as f:
    stats = json.load(f)

# Inicializar variables para determinar el líder en merges
leader = None
max_merges = 0

# Debugging: Print the stats structure to ensure it's as expected
print("Stats structure:", stats)  # Print the structure for debugging

# Verificar que 'users' está en stats
if 'users' in stats:
    # Buscar al usuario con más merges
    for user, data in stats['users'].items():
        if isinstance(data, dict) and 'merge_count' in data:  # Ensure data is a dict and has 'merge_count'
            if data['merge_count'] > max_merges:
                leader = user
                max_merges = data['merge_count']
else:
    print("No 'users' key found in stats")

# Obtener el nombre real del usuario o usar el username si no está en el secret
leader_name = STUDENT_EMAIL_MAP.get(leader, [None, leader])[1]  # Nombre real o username si no existe

# Crear el archivo leaderboard.md con la información
with open('leaderboard.md', 'w') as f:
    f.write('## Ranking de PR Mergeados\n\n')
    f.write(f'El estudiante con más PR mergeados es: **{leader_name}** con **{max_merges}** merges.\n')
