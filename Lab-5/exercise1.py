# Lab 5 - Exercise 1: Campus Resource Tracker
# Course: Programming in Python

resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


def display_resources(resources):
    """Display all resources, handling an empty list and invalid quantities."""
    if not resources:
        print("No resources found.")
        return

    print("ID | Name | Category | Available Quantity")
    for resource in resources:
        resource_id, name, category, quantity = resource
        if quantity < 0:
            print(f"{resource_id} | {name} | {category} | Invalid quantity: {quantity}")
        else:
            print(f"{resource_id} | {name} | {category} | {quantity}")


def search_by_category(resources, category):
    """Display resources matching a category, ignoring letter case."""
    found = False
    for resource in resources:
        if resource[2].lower() == category.lower():
            print(resource)
            found = True

    if not found:
        print(f"No resources found in category: {category}")


def find_unavailable(resources):
    """Display resources whose available quantity is zero."""
    found = False
    for resource in resources:
        if resource[3] == 0:
            print(resource)
            found = True

    if not found:
        print("All resources have at least one unit available.")


def find_resource_by_id(resources, resource_id):
    """Return a resource matching the ID, or None if it does not exist."""
    for resource in resources:
        if resource[0] == resource_id:
            return resource
    return None


if __name__ == "__main__":
    print("ALL RESOURCES")
    display_resources(resources)

    print("\nELECTRONICS RESOURCES")
    search_by_category(resources, "Electronics")

    print("\nUNAVAILABLE RESOURCES")
    find_unavailable(resources)

    print("\nUNKNOWN RESOURCE ID TEST")
    result = find_resource_by_id(resources, 999)
    if result is None:
        print("Resource ID 999 was not found.")

    print("\nEMPTY LIST TEST")
    display_resources([])


    print("\nNEGATIVE QUANTITY TEST")
    test_resources = [[106, "Tablet", "Electronics", -2]]
    display_resources(test_resources)
