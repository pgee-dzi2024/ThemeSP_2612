# main/views.py
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pyautogui


# Това е изгледът за твоя бъдещ HTML/Vue.js frontend
def index(request):
    return render(request, 'main/index.html')


# Това е API endpoint-ът, който ще приема командите от телефона
@api_view(['POST'])
def send_command(request):
    # Вземаме командата от тялото на POST заявката
    command = request.data.get('action')

    # Речник, който свързва нашите команди (от телефона) с реални клавиши за PowerPoint
    commands_map = {
        'next': 'space',
        'prev': 'left',
        'start': 'f5',
        'esc': 'escape',
        'black': 'b',
        'white': 'w'
    }

    if command in commands_map:
        key_to_press = commands_map[command]
        try:
            # Симулираме натискане на клавиш
            pyautogui.press(key_to_press)
            return Response({"status": "success", "message": f"Изпълнена команда: {command}"}, status=200)
        except Exception as e:
            # В случай на грешка с операционната система
            return Response({"status": "error", "message": str(e)}, status=500)
    else:
        return Response({"status": "error", "message": "Непозната команда"}, status=400)