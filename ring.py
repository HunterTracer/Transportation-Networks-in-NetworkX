import networkx as nx


def ring(p_ev):
    p_gv = 1. - p_ev

    od_graph = nx.DiGraph()
    od_graph.add_edges_from([
        (1, 6, {"trip_rate": 14.5}),
        (1, 10, {"trip_rate": 21.75}),
        (1, 11, {"trip_rate": 15.7}),
        (1, 12, {"trip_rate": 11.775}),

        (3, 6, {"trip_rate": 15.3}),
        (3, 10, {"trip_rate": 12.975}),
        (3, 11, {"trip_rate": 12.4}),
        (3, 12, {"trip_rate": 7.85}),

        (4, 9, {"trip_rate": 8.25}),
        (4, 10, {"trip_rate": 11.375}),
        (4, 12, {"trip_rate": 14.9}),
    ])

    gv_od_graph = nx.DiGraph()
    for source, target, data in od_graph.edges(data=True):
        gv_od_graph.add_edge(source, target, trip_rate=data["trip_rate"] * p_gv)

    ev_od_graph = nx.DiGraph()
    for source, target, data in od_graph.edges(data=True):
        ev_od_graph.add_edge(source, target, trip_rate=data["trip_rate"] * p_ev)

    transport_graph = nx.DiGraph()
    transport_graph.add_nodes_from([
        (1,  {"type": "virtual", "capacity": 30., "time": 20. / 60.}),
        (2,  {"type": "regular", "capacity": 0.,  "time": 0.}),
        (3,  {"type": "regular", "capacity": 0.,  "time": 0.}),
        (4,  {"type": "virtual", "capacity": 30., "time": 20. / 60.}),
        (5,  {"type": "virtual", "capacity": 30., "time": 20. / 60.}),
        (6,  {"type": "virtual", "capacity": 30., "time": 20. / 60.}),
        (7,  {"type": "virtual", "capacity": 30., "time": 20. / 60.}),
        (8,  {"type": "virtual", "capacity": 30., "time": 20. / 60.}),
        (9,  {"type": "virtual", "capacity": 30., "time": 20. / 60.}),
        (10, {"type": "regular", "capacity": 0.,  "time": 0.}),
        (11, {"type": "regular", "capacity": 0.,  "time": 0.}),
        (12, {"type": "virtual", "capacity": 30., "time": 20. / 60.}),
    ])
    transport_graph.add_edges_from([
        (1,  2,  {"type": "regular", "capacity": 20.,  "time": 10. / 60.}),
        (1,  3,  {"type": "regular", "capacity": 18.,  "time": 6. / 60.}),
        (1,  4,  {"type": "regular", "capacity": 9.8,  "time": 5. / 60.}),

        (2,  1,  {"type": "regular", "capacity": 20.,  "time": 10. / 60.}),
        (2,  5,  {"type": "regular", "capacity": 7.9,  "time": 5.5 / 60.}),
        (2,  6,  {"type": "regular", "capacity": 17.,  "time": 6.5 / 60.}),

        (3,  1,  {"type": "regular", "capacity": 18.,  "time": 6. / 60.}),
        (3,  4,  {"type": "regular", "capacity": 8.5,  "time": 6. / 60.}),
        (3,  7,  {"type": "regular", "capacity": 19.,  "time": 10.2 / 60.}),

        (4,  1,  {"type": "regular", "capacity": 9.8,  "time": 5. / 60.}),
        (4,  3,  {"type": "regular", "capacity": 8.5,  "time": 6. / 60.}),
        (4,  5,  {"type": "regular", "capacity": 13.5, "time": 12. / 60.}),
        (4,  8,  {"type": "regular", "capacity": 14.,  "time": 11.5 / 60.}),

        (5,  2,  {"type": "regular", "capacity": 7.9,  "time": 5.5 / 60.}),
        (5,  4,  {"type": "regular", "capacity": 13.5, "time": 12. / 60.}),
        (5,  6,  {"type": "regular", "capacity": 8.2,  "time": 6.5 / 60.}),
        (5,  9,  {"type": "regular", "capacity": 13.8, "time": 12.5 / 60.}),

        (6,  2,  {"type": "regular", "capacity": 17.,  "time": 6.5 / 60.}),
        (6,  5,  {"type": "regular", "capacity": 8.2,  "time": 6.5 / 60.}),
        (6,  10, {"type": "regular", "capacity": 20.,  "time": 10.5 / 60.}),

        (7,  3,  {"type": "regular", "capacity": 19.,  "time": 10.2 / 60.}),
        (7,  8,  {"type": "regular", "capacity": 8.9,  "time": 5.8 / 60.}),
        (7,  11, {"type": "regular", "capacity": 17.5, "time": 6.3 / 60.}),

        (8,  4,  {"type": "regular", "capacity": 14.,  "time": 11.5 / 60.}),
        (8,  7,  {"type": "regular", "capacity": 8.9,  "time": 5.8 / 60.}),
        (8,  9,  {"type": "regular", "capacity": 13.2, "time": 11. / 60.}),
        (8,  11, {"type": "regular", "capacity": 9.76, "time": 5.7 / 60.}),

        (9,  5,  {"type": "regular", "capacity": 13.8, "time": 12.5 / 60.}),
        (9,  8,  {"type": "regular", "capacity": 13.2, "time": 11. / 60.}),
        (9,  10, {"type": "regular", "capacity": 9.15, "time": 5.9 / 60.}),
        (9,  12, {"type": "regular", "capacity": 8.97, "time": 5.8 / 60.}),

        (10, 6,  {"type": "regular", "capacity": 20.,  "time": 10.5 / 60.}),
        (10, 9,  {"type": "regular", "capacity": 9.15, "time": 5.9 / 60.}),
        (10, 12, {"type": "regular", "capacity": 18.2, "time": 6.1 / 60.}),

        (11, 7,  {"type": "regular", "capacity": 17.5, "time": 6.3 / 60.}),
        (11, 8,  {"type": "regular", "capacity": 9.76, "time": 5.7 / 60.}),
        (11, 12, {"type": "regular", "capacity": 20.,  "time": 9.8 / 60.}),

        (12, 9,  {"type": "regular", "capacity": 8.97, "time": 5.8 / 60.}),
        (12, 10, {"type": "regular", "capacity": 18.2, "time": 6.1 / 60.}),
        (12, 11, {"type": "regular", "capacity": 20.,  "time": 9.8 / 60.}),
    ])

    return od_graph, gv_od_graph, ev_od_graph, transport_graph


if __name__ == "__main__":
    od_graph, gv_od_graph, ev_od_graph, transport_graph = ring(0.5)
