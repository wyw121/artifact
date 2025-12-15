from access.application import Application
from access.data_repository import DataRepository
import xml.etree.ElementTree as et


class DependencyGraph:
    class Edge:
        def __init__(self, source, dest, count):
            self.source = source
            self.dest = dest
            self.count = count

        def get_source(self):
            return self.source

        def get_dest(self):
            return self.dest

        def get_count(self):
            return self.count

    def __init__(self, application: Application, data_repository: DataRepository):
        self.data_repository = data_repository
        self.application = application
        self.class_edges = []
        self.method_edges = []
        self._setup()

    def _setup(self):
        import csv
        import os
        
        app_name = self.application.get_name()
        
        # Load class edges
        class_csv_path = os.path.abspath(f"./data/relationship_graphs/{app_name}/class_level/structural_static.csv")
        if os.path.exists(class_csv_path):
            with open(class_csv_path, 'r') as f:
                reader = csv.reader(f)
                next(reader) # Skip header
                for row in reader:
                    if len(row) >= 4:
                        source = row[1]
                        dest = row[2]
                        count = int(row[3])
                        self.class_edges.append(DependencyGraph.Edge(source, dest, count))
        else:
            print(f"Warning: {class_csv_path} not found")

        # Load method edges
        method_csv_path = os.path.abspath(f"./data/relationship_graphs/{app_name}/method_level/structural_static.csv")
        if os.path.exists(method_csv_path):
            with open(method_csv_path, 'r') as f:
                reader = csv.reader(f)
                next(reader) # Skip header
                for row in reader:
                    if len(row) >= 4:
                        source = row[1]
                        dest = row[2]
                        count = int(row[3])
                        self.method_edges.append(DependencyGraph.Edge(source, dest, count))
        else:
            print(f"Warning: {method_csv_path} not found")

    def add_edge(self, source, dest, granularity):
        edges = self.method_edges if "method" in granularity else self.class_edges
        count = 1
        existing_edge = next(filter(lambda edge: edge.source == source and edge.dest == dest, edges), None)
        if existing_edge is not None:
            count += existing_edge.get_count()

        if "method" in granularity:
            self.method_edges.append(DependencyGraph.Edge(source, dest, count))
        else:
            self.class_edges.append(DependencyGraph.Edge(source, dest, count))

    def get_direct_usages(self, node, granularity):
        edges = self.method_edges if "method" in granularity else self.class_edges
        return set(map(lambda edge: edge.source, filter(lambda edge: edge.dest == node, edges)))

    def get_indirect_usages(self, node, granularity):
        old_usage_count = 0
        usages = self.get_direct_usages(node, granularity).union([node])

        while len(usages) != old_usage_count:
            old_usage_count = len(usages)
            for usage in usages:
                usages = usages.union(self.get_direct_usages(usage, granularity))

        return usages
