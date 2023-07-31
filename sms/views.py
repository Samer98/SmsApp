import openpyxl
import re
from collections import OrderedDict

from rest_framework import status
import pandas as pd
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import SmsFile
from .serializers import SmsFileSerializer
from rest_framework.views import APIView
from .helper import *

# Create your views here.


class SmsCampaign(ModelViewSet):
    serializer_class = SmsFileSerializer
    queryset = SmsFile.objects.all()

    def create(self, request, *args, **kwargs):
        # Get the uploaded file from the request data
        uploaded_file = request.FILES.get('sms_file')

        if not uploaded_file:
            return Response({'error': 'No file uploaded.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the file is an xlsx file
        if not uploaded_file.name.endswith(('.xlsx', '.csv')):
            return Response({'error': 'Invalid file format. Only xlsx and csv files are allowed.'},
                            status=status.HTTP_400_BAD_REQUEST)

        df = pd.read_excel(uploaded_file)
        # Show the dataframe

        body_message = request.data.get("body_message")
        body_variables = get_words_next_to_dollar(body_message)

        replacement_values = {}
        completed_messages = []
        try:
            for row in range(len(df)):
                excel_value = []
                for var in body_variables:
                    excel_value.append(df[var][row])

                for value in range(len(body_variables)):
                    replacement_values[f"${body_variables[value]}"] = excel_value[value]

                # print(replacement_values)

                completed_messages.append(replace_all(body_message, replacement_values))
            print(completed_messages)
        except:
            return Response({'error': 'The variables in the file is inconsistent'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Continue with the regular create() method to save the instance to the database
        return super().create(request, *args, **kwargs)
