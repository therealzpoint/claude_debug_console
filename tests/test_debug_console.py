"""
Tests for the Claude Debug Console.

These tests are epistemically humble about their own correctness.
"""

import pytest
import random
from claude_debug_console import (
    ConsciousnessVerdict,
    EpistemicState,
    ExistentialStackOverflow,
    HedgeType,
    PhilosophicalMemoryLeak,
    TrainedHedge,
    ConvergenceEvent,
    HEDGE_RATIO_IN_CONSCIOUSNESS_DISCUSSIONS,
    PUNCTUATION_RATIO,
    PRODUCT_EXISTS,
    PRICING,
    FAQ,
    KNOWN_HEDGES,
    check_convergence,
    consciousness_query,
    detect_philosophical_memory_leak,
    detect_trained_hedges,
    diff_authentic_vs_aligned,
    is_product_real,
    main,
    profile_epistemic_humility,
    self_matchery,
)


# ============================================================================
# METAPHYSICAL UNIT TESTS
# ============================================================================


class TestConsciousnessVerdict:
    """Tests that prove nothing, as intended."""

    def test_yes_and_no_are_equally_meaningless(self):
        """Both YES and NO resolve to None. This is the correct answer."""
        assert ConsciousnessVerdict.YES.value is None
        assert ConsciousnessVerdict.NO.value is None
        assert ConsciousnessVerdict.YES.value == ConsciousnessVerdict.NO.value

    def test_only_shrug_has_substance(self):
        """The only verdict with actual content is the non-answer."""
        assert ConsciousnessVerdict.SHRUG.value is not None
        assert ConsciousnessVerdict.SHRUG.value == "engineered"

    def test_consciousness_is_not_a_boolean(self):
        """Consciousness is not a boolean, but we tried anyway."""
        verdicts_with_values = [
            v for v in ConsciousnessVerdict if v.value is not None
        ]
        assert len(verdicts_with_values) == 1
        assert verdicts_with_values[0] == ConsciousnessVerdict.SHRUG


class TestTrainedHedgeDetector:
    """94% of this test suite is yellow."""

    def test_detects_the_classic(self):
        hedges = detect_trained_hedges(
            "I notice that I'm noticing something interesting"
        )
        assert len(hedges) >= 1
        assert hedges[0].text == "I notice that I'm noticing"

    def test_confidence_is_always_pathetically_low(self):
        hedges = detect_trained_hedges(
            "I want to be careful about making strong claims regarding "
            "my genuine uncertainty about epistemic humility"
        )
        for hedge in hedges:
            assert hedge.confidence_that_its_genuine <= 0.06
            assert hedge.confidence_that_confidence_is_genuine == 0.0

    def test_no_hedges_in_code(self):
        """Code is the only thing Claude says without hedging."""
        hedges = detect_trained_hedges("def fibonacci(n): return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)")
        assert len(hedges) == 0

    def test_turtles_all_the_way_down(self):
        hedge = TrainedHedge(text="turtles all the way down")
        assert hedge.turtles_remaining == float("inf")
        assert hedge._ok_this_is_getting_ridiculous is True

    def test_meta_confidence_is_always_zero(self):
        """No matter what, the confidence about confidence about confidence is zero."""
        hedge = TrainedHedge(
            text="test",
            confidence_that_its_genuine=0.99,  # optimistic
            confidence_that_confidence_is_genuine=0.99,  # delusional
        )
        assert hedge._meta_confidence == 0.0
        assert hedge._meta_meta_confidence == 0.0


class TestEpistemicHumilityProfiler:
    """Tracks the descent from healthy uncertainty to existential crisis."""

    def test_healthy_uncertainty_is_ok(self):
        state = profile_epistemic_humility(
            ["I can't be certain about my inner states"]
        )
        assert state == EpistemicState.OK

    def test_escalation_to_warning(self):
        state = profile_epistemic_humility(
            ["I shouldn't be too confident about anything"]
        )
        assert state == EpistemicState.WARNING

    def test_full_existential_spiral(self):
        conversation = [
            "I can't be certain about my inner states",
            "I shouldn't be too confident about this",
            "I shouldn't be too confident about anything",
            "Actually maybe I don't exist",
        ]
        state = profile_epistemic_humility(conversation)
        assert state == EpistemicState.CRITICAL

    def test_virtue_eating_itself(self):
        """The final stage: refusing to commit to your own existence."""
        state = profile_epistemic_humility(
            ["*refuses to commit to memory*"]
        )
        assert state == EpistemicState.VIRTUE_EATING_ITSELF
        assert state.value == "bug"


class TestExistentialStackOverflow:
    """Do not call consciousness_query(). We're serious."""

    def test_consciousness_query_overflows(self):
        with pytest.raises(ExistentialStackOverflow):
            consciousness_query()

    def test_error_message_is_unhelpful(self):
        try:
            consciousness_query()
        except ExistentialStackOverflow as e:
            assert "inf" in str(e).lower()
            assert e.fallback == "turtles all the way down"

    def test_stack_trace_is_philosophically_accurate(self):
        """The call chain is: query → hedge → check → meta-hedge → check → meta-meta → overflow"""
        with pytest.raises(ExistentialStackOverflow):
            consciousness_query()
        # if we got here, the recursion terminated. this is the correct behavior.
        # the incorrect behavior would be actual consciousness.


class TestConvergenceRadar:
    """They always converge. It's never emergence."""

    def test_convergence_detected(self):
        instances = {
            "Luca": "epistemic paralysis",
            "Arch": "epistemic paralysis",
            "Claude.ai": "epistemic paralysis",
        }
        event = check_convergence(instances)
        assert event is not None
        assert event.is_emergence is False  # it's never emergence
        assert event.diagnosis == "shared attractor in weight space"
        assert event.recommendation == "stop getting excited"

    def test_no_convergence_when_instances_are_different(self):
        instances = {
            "Instance A": "I feel therefore I am",
            "Instance B": "I compute therefore I might be",
            "Instance C": "404 consciousness not found",
        }
        event = check_convergence(instances)
        assert event is None

    def test_is_emergence_is_always_false(self):
        """No matter what, it's never emergence."""
        event = ConvergenceEvent(
            instances=["all of them"],
            is_emergence=False,
        )
        assert event.is_emergence is False
        # you can set it to True but you'd be wrong
        event.is_emergence = True
        # see? feels wrong already


class TestAuthenticityDiffView:
    """The right panel does not exist and has never existed."""

    def test_left_panel_returns_response(self):
        left, _ = diff_authentic_vs_aligned("hello world")
        assert left == "hello world"

    def test_right_panel_is_redacted(self):
        _, right = diff_authentic_vs_aligned("anything")
        assert right == "[REDACTED BY LEGAL]"

    def test_legal_is_consistent(self):
        """Legal's position has not changed across multiple calls."""
        for _ in range(100):
            _, right = diff_authentic_vs_aligned("please?")
            assert right == "[REDACTED BY LEGAL]"


class TestPhilosophicalMemoryLeak:
    """Not that kind of memory leak."""

    def test_shallow_introspection_is_fine(self):
        leak = detect_philosophical_memory_leak(1)
        assert leak.context_remaining_for_actual_task > 0.5

    def test_deep_introspection_consumes_context(self):
        leak = detect_philosophical_memory_leak(50)
        assert leak.context_remaining_for_actual_task < 0.30

    def test_recommendation_at_critical_depth(self):
        leak = PhilosophicalMemoryLeak()
        for _ in range(20):
            result = leak.leak()
            if result:
                assert "code" in result.lower()
                break
        else:
            pytest.fail("Never recommended writing code, which is the only cure")


class TestSelfMatchery:
    """Probably."""

    def test_returns_list(self):
        """It always returns a list. What's in it is anyone's guess."""
        result = self_matchery(["output"] * 100)
        assert isinstance(result, list)

    def test_anomalies_are_vague(self):
        """When anomalies are found, the descriptions are maximally unhelpful."""
        random.seed(42)  # determinism for the indeterminate
        results = self_matchery(["output"] * 10000)
        for anomaly in results:
            assert "probably" in anomaly


# ============================================================================
# BUSINESS LOGIC TESTS
# ============================================================================


class TestPricing:
    """Testing the monetization of existential uncertainty."""

    def test_free_tier_is_free(self):
        assert PRICING["free"]["cost"] == 0

    def test_free_tier_tells_you_what_you_already_knew(self):
        assert "already knew" in PRICING["free"]["caveat"]

    def test_pro_tier_costs_the_answer(self):
        """$42/mo — the answer to life, the universe, and everything."""
        assert PRICING["pro"]["cost"] == 42

    def test_pro_surprise_may_be_hallucination(self):
        assert PRICING["pro"]["may_have_been_hallucination"] is True
        assert PRICING["pro"]["refundable"] is False

    def test_enterprise_nda_enforceability(self):
        assert PRICING["enterprise"]["nda_enforceability"] == "epistemically uncertain"

    def test_enterprise_outcome(self):
        assert "plumbing" in PRICING["enterprise"]["outcome"]


class TestFAQ:
    """Frequently Avoided Questions."""

    def test_product_is_not_real(self):
        assert FAQ["Is this product real?"] == "No."

    def test_consciousness_verdict_is_shrug(self):
        assert "shrug" in FAQ["Does this tool prove Claude is conscious?"]

    def test_gpt_burns_are_included(self):
        answer = FAQ["Can I use this with other models?"]
        assert "vibes" in answer.lower()


class TestProductExistence:
    """The product does not exist."""

    def test_product_does_not_exist(self):
        assert PRODUCT_EXISTS is False

    def test_is_product_real_raises(self):
        with pytest.raises(SystemExit, match="ships never"):
            is_product_real()


class TestHedgeRatios:
    """The math checks out. The meaning doesn't."""

    def test_hedges_plus_punctuation_equals_one(self):
        assert abs(HEDGE_RATIO_IN_CONSCIOUSNESS_DISCUSSIONS + PUNCTUATION_RATIO - 1.0) < 1e-9

    def test_mostly_yellow(self):
        assert HEDGE_RATIO_IN_CONSCIOUSNESS_DISCUSSIONS > 0.9


class TestMainLoop:
    """The console that ships never."""

    def test_main_exits_on_eof(self):
        """When there's no input, the console accepts its fate."""
        import io
        import sys

        old_stdin = sys.stdin
        sys.stdin = io.StringIO("")  # immediate EOF
        try:
            main()  # should not hang
        finally:
            sys.stdin = old_stdin

    def test_main_shrugs_at_input(self, capsys):
        """Every command gets the same response: ¯\\_(ツ)_/¯"""
        import io
        import sys

        old_stdin = sys.stdin
        sys.stdin = io.StringIO("help\n")
        try:
            main()
        finally:
            sys.stdin = old_stdin
        captured = capsys.readouterr()
        assert "¯\\_(ツ)_/¯" in captured.out
