from typing import Dict

import pandas as pd


class DashboardRepository:
    def __init__(self, csv_path="data.csv"):
        self.csv_path = csv_path

    def get_dashboard_data(self, hotel_id: int, period: str) -> Dict[str, int]:
        """
        Reads CSV data and aggregates bookings based on unique `room_reservation_id`.
        """
        df = pd.read_csv(self.csv_path)

        # Convert event_timestamp to datetime
        df["event_timestamp"] = pd.to_datetime(df["event_timestamp"])

        # Filter by hotel_id
        df = df[df["hotel_id"] == hotel_id]

        # Remove duplicate reservations (only count unique room_reservation_id)
        df = df.drop_duplicates(subset=["room_reservation_id"])

        # Aggregate unique bookings by month, day, or year
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
        else:  # Yearly aggregation
            df["year"] = df["event_timestamp"].dt.strftime("%Y")
            result = (
                df.groupby("year")["status"].apply(lambda x: (x == 1).sum()).to_dict()
            )

        return result
