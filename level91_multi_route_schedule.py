
print("🚀 Level 91 Multi-Route Schedule Helper")

uni3_am = [
    ["Fremont BART Station", "5:40 AM"],
    ["Stanford Park & Ride", "5:42 AM"],
    ["Fremont Blvd before Mowry", "5:44 AM"],
    ["ACE Centerville Station", "5:50 AM"],
    ["Fremont Blvd before Tamayo St", "5:54 AM"],
    ["Ardenwood Park & Ride", "6:02 AM"],
    ["Embarcadero Rd @ Wildwood", "6:24 AM"],
    ["Campus Oval", "6:33 AM"],
    ["Roth Way Garage", "6:35 AM"],
    ["Psychiatry Parking Lot", "6:37 AM"],
    ["Quarry Rd @ Psychiatry Bldg", "6:39 AM"],
]

uni3_pm = [
    ["Stockfarm Garage", "3:25 PM"],
    ["Campus Oval", "3:35 PM"],
    ["Roth Way Garage", "3:38 PM"],
    ["Psychiatry Parking Lot", "3:41 PM"],
    ["Quarry Rd & Psychiatry Building", "3:44 PM"],
    ["Embarcadero Rd @ N. California Ave", "3:55 PM"],
    ["Ardenwood Park & Ride", "4:27 PM"],
    ["Fremont Blvd After Tamayo St", "4:39 PM"],
    ["ACE Centerville Station", "4:43 PM"],
    ["Fremont Blvd After Mowry Ave", "4:47 PM"],
    ["Stanford Park & Ride", "4:50 PM"],
    ["Fremont BART Station", "4:56 PM"],
]

schedules = {
    "UNI 3 AM": uni3_am,
    "UNI 3 PM": uni3_pm,
}

while True:
    print("\n1. Show All Route Names")
    print("2. Show One Route Schedule")
    print("3. Search Stop in All Routes")
    print("4. Show All Route Summary")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "1":
        print("\n🚌 Route Names")
        print("----------------")
        for route_name in schedules:
            print(route_name)

    elif choice == "2":
        route = input("Enter route name, example UNI 3 AM: ").upper()

        if route in schedules:
            print("\n🚌", route)
            print("----------------")
            for stop, time in schedules[route]:
                print(time, "-", stop)
        else:
            print("Route not found ❌")

    elif choice == "3":
        search = input("Enter stop name to search: ").lower()

        print("\n🔍 Search Results")
        found = False

        for route_name, route_schedule in schedules.items():
            for stop, time in route_schedule:
                if search in stop.lower():
                    print(route_name + ":", time, "-", stop)
                    found = True

        if found == False:
            print("Stop not found ❌")

    elif choice == "4":
        print("\n📊 All Route Summary")
        print("----------------")

        for route_name, route_schedule in schedules.items():
            print("\nRoute:", route_name)
            print("Stops:", len(route_schedule))
            print("Start:", route_schedule[0][1], "-", route_schedule[0][0])
            print("End:", route_schedule[-1][1], "-", route_schedule[-1][0])

    elif choice == "5":
        print("Goodbye Phillip! 👋")
        break

    else:
        print("Invalid choice ❌")