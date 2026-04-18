from django.core.management.base import BaseCommand
from apps.products.models import Product

class Command(BaseCommand):
    help = 'Populate database with ice cream products'

    def handle(self, *args, **options):
        products_data = [
            {
                'name': 'Vanilla',
                'description': 'Classic vanilla ice cream with a smooth, creamy taste. The perfect choice for any occasion.',
                'price': 3.99,
                'image': 'src/assets/images/vanilla.jpg'
            },
            {
                'name': 'Berry Burst Layer',
                'description': 'Delightful layers of mixed berry flavors - blueberry, raspberry, and strawberry combined!',
                'price': 5.49,
                'image': 'src/assets/images/Berry_Burst_Layer.jpg'
            },
            {
                'name': 'Chocolate',
                'description': 'Rich and creamy chocolate ice cream made from premium cocoa. Perfect for chocolate lovers!',
                'price': 4.99,
                'image': 'src/assets/images/Chocolate.jpg'
            },
            {
                'name': 'Mango',
                'description': 'Tropical mango ice cream with a vibrant, fruity flavor. Pure summer in every scoop!',
                'price': 4.79,
                'image': 'src/assets/images/mango.jpg'
            },
            {
                'name': 'Strawberry Splash',
                'description': 'Fresh and fruity strawberry ice cream. Made with real strawberry flavor for authentic taste.',
                'price': 4.49,
                'image': 'src/assets/images/Strawberry_Splash.jpg'
            },
            {
                'name': 'Coffee Chill Blast',
                'description': 'Smooth coffee ice cream with an invigorating caffeine kick. Perfect for coffee enthusiasts!',
                'price': 5.29,
                'image': 'src/assets/images/Coffee_Chill_Blast.jpg'
            },
            {
                'name': 'Blueberry',
                'description': 'Antioxidant-rich blueberry ice cream with a sweet and tangy taste. Healthy indulgence!',
                'price': 4.89,
                'image': 'src/assets/images/Blueberry.jpg'
            },
            {
                'name': 'Nutty Nutella Swirl',
                'description': 'Creamy Nutella swirled throughout vanilla ice cream. A chocolate hazelnut dream!',
                'price': 5.99,
                'image': 'src/assets/images/Nutty_Nutella_Swirl.jpg'
            },
            {
                'name': 'Pineapple',
                'description': 'Tropical pineapple ice cream with bright, refreshing flavors. Beach vibes guaranteed!',
                'price': 4.59,
                'image': 'src/assets/images/Pineapple.jpg'
            },
            {
                'name': 'Apple Frost Delight',
                'description': 'Cool apple ice cream with a hint of cinnamon spice. A delightful autumn treat!',
                'price': 4.69,
                'image': 'src/assets/images/Apple_Frost.jpg'
            },
            {
                'name': 'Orange Zest Scoop',
                'description': 'Sunny orange ice cream with fresh citrus zest. Bright and refreshing flavor!',
                'price': 4.79,
                'image': 'src/assets/images/Orange_Zest_Scoop.jpg'
            },
            {
                'name': 'Grape Galaxy',
                'description': 'Exotic grape ice cream with a cosmic purple hue. Out of this world delicious!',
                'price': 4.89,
                'image': 'src/assets/images/Grape_Galaxy.jpg'
            },
            {
                'name': 'Coconut Tropical Cream',
                'description': 'Creamy coconut ice cream with tropical vibes. Transport yourself to paradise!',
                'price': 5.19,
                'image': 'src/assets/images/Coconut_Tropical_Cream.jpg'
            },
            {
                'name': 'Watermelon Ice',
                'description': 'Cool and refreshing watermelon ice cream. Perfect summer delight!',
                'price': 4.49,
                'image': 'src/assets/images/Watermelon_ice.jpg'
            },
            {
                'name': 'Papaya',
                'description': 'Smooth papaya ice cream with tropical sweetness. Golden and delicious!',
                'price': 4.69,
                'image': 'src/assets/images/Papaya.jpg'
            },
            {
                'name': 'Pistachio Ice Cream',
                'description': 'Premium pistachio ice cream with nutty richness. An elegant choice!',
                'price': 5.39,
                'image': 'src/assets/images/Pistachio_Ice_Cream.jpg'
            },
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'image': product_data['image'],
                }
            )
            if created:
                self.stdout.write(f'Successfully created {product.name}')
            else:
                self.stdout.write(f'{product.name} already exists')
