import os
from typing import Dict

import pandas as pd


class DashboardRepository:
    def __init__(self, csv_path=None):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
        self.csv_path = csv_path or os.path.join(base_dir, "data.csv")

    def get_dashboard_data(self, hotel_id: int, period: str) -> Dict[str, int]:
        """
        Reads CSV data and aggregates bookings based on  `room_reservation_id`.
        """
        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"Error: CSV file not found at {self.csv_path}")

        try:
            df = pd.read_csv(self.csv_path)
        except Exception as e:
            raise Exception(f"Error loading CSV file: {str(e)}")

        # Ensure columns exist
        required_columns = [
            "hotel_id",
            "event_timestamp",
            "room_reservation_id",
            "status",
        ]
        for col in required_columns:
            if col not in df.columns:
                raise Exception(f"Missing column in CSV: {col}")

        # Convert event_timestamp to datetime
        df["event_timestamp"] = pd.to_datetime(df["event_timestamp"], errors="coerce")

        # Remove invalid timestamps
        if df["event_timestamp"].isnull().sum() > 0:
            raise Exception("Invalid dates found in event_timestamp")

        # Filter by hotel_id
        df = df[df["hotel_id"] == hotel_id]

        # Remove duplicate reservations
        df = df.drop_duplicates(subset=["room_reservation_id"])

        # unique bookings by month, day, or year
        if period == "month":
            df["month"] = df["event_timestamp"].dt.strftime("%Y-%m")
            result = (
                df.groupby("month")["status"].apply(lambda x: (x == 1).sum()).to_dict()
            )
        elif period == "day":
            df["day"] = df["event_timestamp"].dt.strftime("%Y-%m-%d")
            result = (
                df.groupby("day")["status"].apply(lambda x: (x == 1).sum()).to_dict()
            )
        else:  # Yearly
            df["year"] = df["event_timestamp"].dt.strftime("%Y")
            result = (
                df.groupby("year")["status"].apply(lambda x: (x == 1).sum()).to_dict()
            )

        return result
