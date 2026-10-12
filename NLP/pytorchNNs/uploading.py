from huggingface_hub import HfApi

api = HfApi()

def ask_for_address(repo_id: str, private: bool = False):
    api.create_repo(repo_id=repo_id, private=private)
    return f"Repositorio '{repo_id}' creado exitosamente."

def upload(path: str, name: str, repo_id: str):
    api.upload_file(
        path_or_fileobj=path,
        path_in_repo=name,
        repo_id=repo_id
    )
    return f"Archivo '{name}' subido a '{repo_id}'."

# 🖥️ Interacción por consola
if __name__ == "__main__":
    repo_id = input("🔧 Ingresa el nombre del repositorio (ej. daniel/modelo-nlp): ")
    privado = input("¿Quieres que el repositorio sea privado? (True,false): ").lower() == "True"
    print(ask_for_address(repo_id, private=privado))

    path = input("📁 Ruta del archivo a subir: ")
    name = input("📄 Nombre del archivo dentro del repositorio: ")
    print(upload(path, name, repo_id))
