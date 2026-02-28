import React, { useState } from "react";
import {
  Container,
  TextField,
  Button,
  Typography,
  Box,
  Grid,
  Card,
  CardContent,
  LinearProgress,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  Divider
} from "@mui/material";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";

function App() {
  const [worldPrompt, setWorldPrompt] = useState("");
  const [world, setWorld] = useState(null);
  const [action, setAction] = useState("");
  const [log, setLog] = useState([]);
  const [tension, setTension] = useState(0);
  const [loading, setLoading] = useState(false);

  const createWorld = async () => {
    setLoading(true);
    const res = await fetch("http://localhost:8000/create-world", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt: worldPrompt })
    });

    const data = await res.json();
    setWorld(data);
    setLoading(false);
  };

  const playTurn = async () => {
    if (!action) return;

    const res = await fetch("http://localhost:8000/turn", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action })
    });

    const data = await res.json();

    setLog([data, ...log]);
    setTension(data.tension);
    setAction("");
  };

  return (
    <Container
      maxWidth="lg"
      sx={{
        mt: 4,
        color: "white",
        minHeight: "100vh",
        backgroundColor: "#f6f8ff",
        padding: 4,
        borderRadius: 3
      }}
    >
      <Typography variant="h4" gutterBottom sx={{ fontWeight: "bold" }}>
        🧠 Autonomous Multi-Agent Game Master
      </Typography>

      {/* WORLD CREATION */}
      {!world && (
        <Card sx={{ backgroundColor: "#1a1d25", p: 3 }}>
          <Typography variant="h6" gutterBottom>
            Create Your World
          </Typography>

          <TextField
            fullWidth
            variant="outlined"
            label="Describe your world idea..."
            value={worldPrompt}
            onChange={(e) => setWorldPrompt(e.target.value)}
            sx={{ backgroundColor: "white", borderRadius: 1 }}
          />

          <Button
            variant="contained"
            sx={{ mt: 2 }}
            onClick={createWorld}
            disabled={loading}
          >
            {loading ? "Generating..." : "Generate World"}
          </Button>
        </Card>
      )}

      {/* GAME INTERFACE */}
      {world && (
        <>
          <Grid container spacing={3} sx={{ mt: 2 }}>
            {/* WORLD PANEL */}
            <Grid item xs={6}>
              <Card sx={{ backgroundColor: "#ccd6f2" }}>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    🌍 World Overview
                  </Typography>

                  <Typography variant="h5" sx={{ fontWeight: "bold" }}>
                    {world.name}
                  </Typography>

                  <Typography
                    variant="body2"
                    sx={{ mt: 1, lineHeight: 1.8 }}
                  >
                    {world.description}
                  </Typography>

                  <Divider sx={{ my: 2, backgroundColor: "#f0dada" }} />

                  <Typography variant="body1">
                    🔥 Tension Level
                  </Typography>

                  <LinearProgress
                    variant="determinate"
                    value={Math.min(tension * 10, 100)}
                    sx={{ mt: 1, height: 10, borderRadius: 5 }}
                  />

                  <Divider sx={{ my: 2, backgroundColor: "#eecaca" }} />

                  <Typography variant="body1" gutterBottom>
                    📍 Locations
                  </Typography>

                  {world.locations?.map((loc, i) => (
                    <Typography key={i} variant="body2">
                      • {loc}
                    </Typography>
                  ))}
                </CardContent>
              </Card>
            </Grid>

            {/* NPC PANEL */}
            <Grid item xs={6}>
              <Card sx={{ backgroundColor: "#9fa7bd" }}>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    🤖 Active Agents
                  </Typography>

                  {world.npcs?.map((npc, index) => (
                    <Box key={index} sx={{ mb: 2 }}>
                      <Typography sx={{ fontWeight: "bold" }}>
                        {npc.name}
                      </Typography>
                      <Typography variant="body2" sx={{ color: "#584747" }}>
                        Goal: {npc.goal}
                      </Typography>
                      <Divider sx={{ my: 1, backgroundColor: "#e0c7c7" }} />
                    </Box>
                  ))}
                </CardContent>
              </Card>
            </Grid>
          </Grid>

          {/* PLAYER INPUT */}
          <Box sx={{ mt: 4 }}>
            <TextField
              fullWidth
              variant="outlined"
              label="Enter your action..."
              value={action}
              onChange={(e) => setAction(e.target.value)}
              sx={{ backgroundColor: "white", borderRadius: 1 }}
            />

            <Button
              variant="contained"
              color="secondary"
              sx={{ mt: 2 }}
              onClick={playTurn}
            >
              Execute Turn
            </Button>
          </Box>

          {/* LOG SECTION */}
          <Box sx={{ mt: 5 }}>
            <Typography variant="h5" gutterBottom>
              📜 Simulation Log
            </Typography>

            {log.map((entry, index) => (
              <Card
                key={index}
                sx={{
                  mt: 2,
                  backgroundColor: "#8792b1",
                  borderLeft: "5px solid #4caf50"
                }}
              >
                <CardContent>
                  <Typography
                    variant="subtitle2"
                    sx={{ color: "#888" }}
                  >
                    Turn {log.length - index}
                  </Typography>

                  <Typography
                    variant="h6"
                    sx={{ mt: 1, color: "#0d270d" }}
                  >
                    🎯 Game Master Outcome
                  </Typography>

                  <Typography
                    variant="body2"
                    sx={{ whiteSpace: "pre-line", lineHeight: 1.8 }}
                  >
                    {entry.outcome}
                  </Typography>

                  <Divider sx={{ my: 2, backgroundColor: "#333" }} />

                  <Typography
                    variant="h6"
                    sx={{ color: "#2196f3" }}
                  >
                    🤖 Agent Reasoning
                  </Typography>

                  {entry.agents.map((agentText, i) => {
                    const name = agentText.split(":")[0];
                    const reasoning = agentText.split(":").slice(1).join(":");

                    return (
                      <Accordion
                        key={i}
                        sx={{
                          mt: 1,
                          backgroundColor: "#12141b",
                          color: "white"
                        }}
                      >
                        <AccordionSummary
                          expandIcon={
                            <ExpandMoreIcon sx={{ color: "white" }} />
                          }
                        >
                          <Typography sx={{ fontWeight: "bold" }}>
                            {name}
                          </Typography>
                        </AccordionSummary>

                        <AccordionDetails>
                          <Typography
                            variant="body2"
                            sx={{
                              whiteSpace: "pre-line",
                              lineHeight: 1.7,
                              color: "#ccc"
                            }}
                          >
                            {reasoning}
                          </Typography>
                        </AccordionDetails>
                      </Accordion>
                    );
                  })}
                </CardContent>
              </Card>
            ))}
          </Box>
        </>
      )}
    </Container>
  );
}

export default App;