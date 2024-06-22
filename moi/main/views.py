from django.shortcuts import render
from django.http import JsonResponse
from .models import Image, Placemark, Route

def map(request):
    if request.GET.get('route'):
        route_id =int(request.GET.get('route'))
        try:
            selected_route = Route.objects.get(id=route_id)
            # route_placemarks = Placemark.objects.filter(id=route_id)
            # print(selected_route.placemarks)
        except Route.DoesNotExist:
            return JsonResponse({}, status=404)
        return JsonResponse({
            'name': selected_route.name,
            'descripion': selected_route.descripion,
            'type': selected_route.type.name,
            'difficult': selected_route.difficult,
            'lenght': selected_route.lenght,
            'main_image': selected_route.main_image.file.path,
            'additional_images': list(selected_route.additional_images.values('alt', 'file')),
            'gpx': selected_route.gpx.path,
                # 'placemarks': selected_route.placemarks
            },
            status=200,
            json_dumps_params={'ensure_ascii': False})
    return render(request, 'main/index.html')
