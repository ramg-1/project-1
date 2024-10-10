import os
import random
from faker import Faker
from django.core.files import File

# Set the environment variable for Django settings before importing the models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')  
import django
django.setup()

from properties.models import Property  # Now you can import your model

fake = Faker()

def generate_dummy_properties(num_properties=50):
    # List of images available
    image_files = [f'image-{i}.jpeg' for i in range(1, 11)]  # Change the extension if your images are .jpg

    for _ in range(num_properties):
        title = fake.catch_phrase()
        description = fake.text(max_nb_chars=200)
        price = random.randint(100000, 1000000) 
        bedrooms = random.randint(1, 5)
        bathrooms = random.randint(1, 3)  
        area = random.randint(500, 5000)  
        address = fake.address()

        # Randomly select an image file from the list
        selected_image = random.choice(image_files)
        image_path = os.path.join('media/dummy_images', selected_image)  # Update this path to your images folder
        
        try:
            with open(image_path, 'rb') as image_file:
                property_image = File(image_file)
                property_instance = Property(
                    title=title,
                    description=description,
                    price=price,
                    bedrooms=bedrooms,
                    bathrooms=bathrooms,
                    area=area,
                    address=address,
                    image=property_image
                )
                property_instance.save()
                print(f'Saved Property: {title} with image: {selected_image}')
        except FileNotFoundError:
            print(f'Image file not found: {image_path}')

if __name__ == '__main__':
    generate_dummy_properties()
