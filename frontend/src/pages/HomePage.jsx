import React, { useState, useEffect } from "react";
import { toast } from "sonner";
import Header from "@/components/Header";
import AddTask from "@/components/AddTask";
import StatsAndFilters from "@/components/StatsAndFilters";
import TaskList from "@/components/TaskList";
import TaskListPagination from "@/components/TaskListPagination";
import DateTimeFilters from "@/components/DateTimeFilter";
import Footer from "@/components/Footer";
import api from "@/lib/axios";
import { visibleTaskLimit } from "@/lib/data";


const HomePage = () => {
    const [taskBuffer, setTaskBuffer] = useState([]);
    const [activeTaskCount, setActiveTaskCount] = useState(0);
    const [completeTaskCount, setCompleteTaskCount] = useState(0);
    const [filter, setFilter] = useState("all");
    const [dateQuery, setDateQuery] = useState("today");
    const [page, setPage] = useState(1);

    const fetchTasks = async () => {
        try {
            const res = await api.get(`/tasks?filter=${dateQuery}`);
            setTaskBuffer(res.data.tasks);
            setActiveTaskCount(res.data.active_count);
            setCompleteTaskCount(res.data.complete_count);
        } catch (error) {
            console.error("An error occurred while fetching tasks:", error);
            toast.error("An error occurred while fetching tasks");
        }
    };

    useEffect(() => {
        fetchTasks();
    }, [dateQuery]);

    useEffect(() => {
        setPage(1);
    }, [filter, dateQuery]);

    const handleTaskChanged = () => {
        fetchTasks();
    };

    const handleNext = () => {
        if (page < totalPages) {
            setPage((prev) => prev + 1);
        }
    };

    const handlePrev = () => {
        if (page > 1) {
            setPage((prev) => prev - 1);
        }
    };

    const handlePageChanged = (newPage) => {
        setPage(newPage);
    };

    const filteredTasks = taskBuffer.filter((task) => {
        switch (filter) {
            case "active":
                return task.status === "active";
            case "complete":
                return task.status === "complete";
            default:
                return true;
        }
    });

    const visibleTasks = filteredTasks.slice(
        (page - 1) * visibleTaskLimit,
        page * visibleTaskLimit
    );

    if (visibleTasks.length === 0) {
        handlePrev();
    }

    const totalPages = Math.ceil(filteredTasks.length / visibleTaskLimit);

    return (
        <div className="min-h-screen w-full bg-[#fefcff] relative">
            <div
                className="absolute inset-0 z-0"
                style={{
                    backgroundImage: `
                radial-gradient(circle at 30% 70%, rgba(173, 216, 230, 0.35), transparent 60%),
                radial-gradient(circle at 70% 30%, rgba(255, 182, 193, 0.4), transparent 60%)`,
                }}
            />
            <div className="container pt-8 mx-auto relative z-10">
                <div className="w-full max-w-2xl p-6 mx-auto space-y-6">
                    <Header/>
                    <AddTask handleNewTaskAdded={handleTaskChanged}/>
                    <StatsAndFilters
                        filter={filter}
                        setFilter={setFilter}
                        activeTaskCount={activeTaskCount}
                        completeTaskCount={completeTaskCount}
                    />
                    <TaskList 
                        filteredTasks={visibleTasks}
                        filter={filter}
                        handleTaskChanged={handleTaskChanged}
                    />
                    <div className="flex flex-col items-center justify-between gap-6 sm:flex-row">
                        <TaskListPagination
                            handleNext={handleNext}
                            handlePrev={handlePrev}
                            handlePageChanged={handlePageChanged}
                            page={page}
                            totalPages={totalPages}
                        />
                        <DateTimeFilters 
                            dateQuery={dateQuery} 
                            setDateQuery={setDateQuery}
                        />
                    </div>
                    <Footer
                        activeTaskCount={activeTaskCount}
                        completeTaskCount={completeTaskCount}
                    />
                </div>
            </div>
        </div>
    );
};


export default HomePage;