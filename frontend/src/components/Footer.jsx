import React from "react";

const Footer = ({ completeTaskCount = 0, activeTaskCount = 0 }) => {
    return <>
        {completeTaskCount + activeTaskCount > 0 && (
            <div className="text-center">
                <p className="text-sm text-muted-foreground">
                    {
                        completeTaskCount > 0 && (
                            <>
                                🎉 Great! You have completed {completeTaskCount} task
                                {completeTaskCount > 1 ? 's' : ''} 
                                {activeTaskCount > 0 && `, only ${activeTaskCount} more to go. Keep it up!`}
                            </>
                        )
                    }

                    {
                        completeTaskCount === 0 && activeTaskCount > 0 && (
                            <>
                                🚀 Let's get started with {activeTaskCount} task
                                {activeTaskCount > 1 ? 's' : ''}
                            </>
                        )
                    }
                </p>
            </div>
        )}
    </>;
};

export default Footer;