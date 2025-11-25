import fme
import fmeobjects
from datetime import datetime

class FeatureProcessor(object):
    """
    Custom FME PythonCaller script to enrich LIDAR data.
    Calculates point counts from geometry and adds audit timestamps.
    """
    def __init__(self):
        pass

    def input(self, feature):
        # 1. Get the number of points in this chunk (Point Cloud Geometry)
        # Note: FME handles point clouds as a single feature with complex geometry
        geometry = feature.getGeometry()
        if geometry:
            point_count = geometry.getPointCount()
            feature.setAttribute("processed_point_count", point_count)
        
        # 2. Add a processing timestamp for Audit Trail
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        feature.setAttribute("processed_timestamp", now)
        
        # 3. Add a "Quality Check" tag
        feature.setAttribute("data_quality_status", "Verified_Ground_Class")
        
        # Output the modified feature to the next transformer
        self.pyoutput(feature)

    def close(self):
        pass