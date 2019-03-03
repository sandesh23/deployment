from rest_framework.routers import SimpleRouter
from .views import *

router= SimpleRouter()

router.register("Address",AddressViewSet)
router.register("Customer",CustomerViewSet)
router.register("Hotel",HotelViewSet)
router.register("Menu",MenuViewSet)
router.register("Waiter",WaiterViewSet)
router.register("Maneger",ManagerViewSet)
urlpatterns =router.urls