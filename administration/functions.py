import time
import pandas as pd
from .models import Items, Supplier

def load_data(file, supplier):
    try:
        df = pd.read_excel(file)
    except:
        return {'status': 'error', 'message': 'El archivo no es excel válido.'}

    Items.objects.filter(supplier=supplier).delete()
    selected_supplier = Supplier.objects.get(id=supplier)

    start_time = time.time()
    processed_count = 0

    for index, row in df.iterrows():
        item_data = row.to_dict()
        image_url = f"{'https://s3.amazonaws.com/distribuidoradm/'}{item_data['Código'].replace('/', '-')}.jpg"

        item = Items(
            description=item_data['Descripción'],
            origin=item_data['Origen'],
            price=round(item_data['Precio de Lista'] * 1.21),
            supplier=selected_supplier,
            image=image_url
        )

        item.save()
        processed_count += 1

    end_time = time.time()
    total_time = end_time - start_time

    return f"Se procesaron {processed_count} productos en {total_time:.2f} segundos."

def delete_data():
    if Items.objects.exists():
        Items.objects.all().delete()
        return {'status': 'success', 'message': 'Datos eliminados correctamente.'}
    else:
        return {'status': 'warning', 'message': 'No hay datos para eliminar.'}