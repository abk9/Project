from rest_framework import permissions

class IsEditorOrReadOnly(permissions.BasePermission):
    """
    Permission personnalisée :
    - Autorise la lecture (GET, HEAD, OPTIONS) à tous les utilisateurs authentifiés.
    - Autorise l'écriture (POST, PUT, DELETE) uniquement aux membres du groupe 'Editor' ou aux super-administrateurs.
    """
    
    def has_permission(self, request, view):
        # On s'assure d'abord que l'utilisateur est bien connecté
        if not request.user or not request.user.is_authenticated:
            return False

        # Si la requête est une méthode de lecture (GET, etc.), on autorise l'accès
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Si c'est une méthode de modification (POST, PUT, DELETE),
        # on vérifie si l'utilisateur est super-admin OU s'il appartient au groupe 'Editor'
        is_editor = request.user.groups.filter(name='Editor').exists()
        return is_editor or request.user.is_superuser