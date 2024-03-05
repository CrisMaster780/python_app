def get_related_instances(instance):
    """
    Obtiene relaciones activas de una instancia de modelo.

    Esta función recibe una instancia de modelo y busca todas las relaciones
    inversas definidas en la instancia. Luego, verifica si hay instancias
    relacionadas activas para cada relación, donde el campo 'status' tiene el
    valor 1.

    Args:
        instance: La instancia de modelo para la que se buscan relaciones activas.

    Returns:
        Una lista de relaciones inversas activas.
    """
    # Obtener las relaciones de la instancia
    related_objects = instance._meta.related_objects
    active_relations = []

    # Iterar a través de las relaciones
    for related_object in related_objects:
        related_name = related_object.get_accessor_name()

        # Verificar si hay instancias relacionadas activas para esta relación
        try:
            related_instances = getattr(instance, related_name).filter(estado=1)

            # Si hay instancias relacionadas activas, agregar esta relación a la lista
            if related_instances.exists():
                active_relations.append(related_object)
        except AttributeError:
            pass  # La relación no existe en esta instancia

    return active_relations