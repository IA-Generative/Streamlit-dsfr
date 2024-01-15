<script setup lang="ts">
import { onMounted, onUnmounted, reactive, ref, watch } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrButton } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps.d.ts'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		label?: string | undefined
		secondary?: boolean
		tertiary?: boolean
		disabled?: boolean
		icon?: string | undefined
		iconOnly?: boolean
		iconRight?: boolean
		noOutline?: boolean
		size?: '' | 'small' | 'sm' | 'lg' | 'large' | 'md' | 'medium'
	}>
>()

// Default props values
watch(() => props.args, () =>
	{
		props.args.label ||= 'Button'
		props.args.secondary ??= false
		props.args.tertiary ??= false
		props.args.disabled ??= false
		props.args.iconOnly ??= false
		props.args.iconRight ??= false
		props.args.noOutline ??= false
		props.args.size ??= ''
	},
	{ deep: true, immediate: true },
)

const clicked = ref(false)
const isFocused = ref(false)

const onRenderEvent = (_event: Event): void =>
	{
		if (!isFocused.value && clicked.value)
		{
			clicked.value = false
			Streamlit.setComponentValue(clicked.value)
		}
	}

onMounted(() =>
	{
		Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

onUnmounted(() =>
	{
		Streamlit.events.removeEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

const onClick = () =>
	{
		if (!clicked.value)
		{
			clicked.value = true
			Streamlit.setComponentValue(clicked.value)
		}
	}

const onFocus = () =>
	{
		isFocused.value = true
	}

const onBlur = () =>
	{
		isFocused.value = false
	}
</script>

<template>
	<div class="component" :style="style">
		<DsfrButton
			:label="props.args.label"
			:secondary="props.args.secondary"
			:tertiary="props.args.tertiary"
			:disabled="props.disabled || props.args.disabled"
			:icon="props.args.icon"
			:size="props.args.size"
			:no-outline="props.args.noOutline"
			:icon-only="props.args.iconOnly"
			:icon-right="props.args.iconRight"
			@click="onClick"
			@focus="onFocus"
			@blur="onBlur"
		/>
	</div>
</template>
