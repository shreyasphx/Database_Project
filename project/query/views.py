#views.py

from rest_framework import viewsets

from .serializers import QuerySerializer
from .models import Query
import psycopg2
import sqlite3
import pandas

class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all().order_by('name')
    serializer_class = QuerySerializer

    @action(detail=True, methods=['get'])
    def executeQuery(self, request, pk):
        query = self.get_object()
        try:
            cnx = psycopg2.connect(
                host=query.connection.host,
                database=query.connection.dbname,
                user=query.connection.user,
                password=query.connection.password,
                port=query.connection.port
            )
            cursor = cnx.cursor(buffered=True)
            cursor.execute(query.query)
            result_df = DataFrame(cursor.fetchall())
            result_df.columns = cursor.column_names
            cnx.close()
            file_name=query.name + ".xlsx"
            result_df.to_excel(file_name)
            return Response({'status':'success!'})
        except psycopg2.Error as err:
            print("Error connecting to postgresql database: " + str(err))
            return Response({'status':'failure!'})

