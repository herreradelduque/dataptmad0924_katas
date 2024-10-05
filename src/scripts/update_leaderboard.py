import json
import os

# Obtener datos del secret
students = json.loads(os.environ['STUDENT_EMAIL_MAP'])

# Leer pr_stats.json
with open('pr_stats.json', 'r') as f:
    stats = json.load(f)

# Buscar al usuario con más merges
leader = None
max_merges = 0

for user, data in stats['users'].items():
    if data['merge_count'] > max_merges:
        leader = user
        max_merges = data['merge_count']

# Obtener nombre real del secret o usar el username si no está en el secret
leader_name = students.get(leader, [None, leader])[1]  # Nombre real o username si no existe

# Crear leaderboard.md
with open('leaderboard.md', 'w') as f:
    f.write('## Ranking de PR Mergeados\\n\\n')
    f.write(f'El estudiante con más PR mergeados es: **{leader_name}** con **{max_merges}** merges.\\n')
